from .import bp as shop_bp
from flask import render_template, redirect, url_for, flash, request
from app.blueprints.shop.models import Product, Cart
from app.blueprints.auth.models import User
from app.blueprints.billboard.models import Song
from flask_login import current_user
from app import db
import os
from dotenv import load_dotenv
import pandas as pd
import sqlalchemy

@shop_bp.route('/')
def home():
    context = {
        'products': Product.query.all()
    }
    return render_template('shop/home.html', **context)

@shop_bp.route('/product/add')
def add_product():
    try:
        _id = request.args.get('id')
        print(f'This is the ID: {_id}')

        p = Product.query.get(_id)
        print(f'This is the product object: {p}')

        c = Cart(user_id=current_user.id, product_id=p.id)
        c.save()
        flash(f'{p.song_name} was added successfully', 'success')
    except Exception as error:
        flash(f'{p.song_name} was not added successfully. Try again.', 'success')

    return redirect(url_for('shop.home'))

@shop_bp.route('/cart')
def cart():
    context = {}
    return render_template('shop/cart.html', **context)


# FIX ME! For some reason when I delete some items other items get deleted.  the product number looks good though
@shop_bp.route('/cart/delete')
def delete_product():
    p = Product.query.get(request.args.get('product_id'))
    cart = current_user.cart
    for i in cart:
        if i.product_id ==p.id and current_user.id == i.user_id:
            cart_item = Cart.query.filter_by(user_id=current_user.id).first()
            print(cart_item)
            db.session.delete(cart_item)
    db.session.commit()
    cart_item = Cart.query.filter_by(product_id=p.id).first()
    flash('Product delete', 'info')
    return redirect(url_for('shop.cart'))

@shop_bp.route('/checkout')
def checkout():
    context = {}
    return render_template('shop/checkout.html', **context)

@shop_bp.route('/billboard/product_creation', methods=['POST'])
def product_creation():
    if request.method == 'POST':
        # THIS WILL PULL ALL SONG DATA FROM THE DATABASE AND GET UNIQUE VALUES -------------------------
        engine = sqlalchemy.create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'))
        sql_data = pd.read_sql_table('song',engine)

        song_unique_dataset = sql_data[['song_name','song_artist', 'song_name_artist_combined','song_picture']]
        song_unique_dataset.drop_duplicates(inplace=True)

        print("-"*100)
        print(f'List of dates: {song_unique_dataset[0:10]}')
        song_record_total_count = len(song_unique_dataset)
        print(f'Total counts of dates: {song_record_total_count}')
        print("-"*100)

        # num_dates_listed = pd.unique(dates_dataset['new_date'])
        # print("-"*100)
        # print(f'List of dates: {num_dates_listed}')
        # num_dates_total_count = len(num_dates_listed)
        # print(f'Total counts of dates: {num_dates_total_count}')
        # print("-"*100)
        
        # THIS WILL CHECK WHAT EXISTS ALREADY --------------------------------------------------
        sql_data_products = pd.read_sql_table('product',engine)
        product_unique_dataset = sql_data_products
        list_of_products = []
        list_of_products = product_unique_dataset['song_name_artist_combined'].tolist()
        print("+"*100)
        print(list_of_products[0:20])
        print("+"*100)

         # THIS ADD TO THE PRODUCT DATABASE IF IT IS A NEW ITEM --------------------------------------------------
        # for index, row in song_unique_dataset.head(n=6).iterrows():
        #     print(f'Index: {index}; Name: {row["song_name"]}; Artist: {row["song_artist"]}; ID: {row["song_name_artist_combined"]}; Picture: {row["song_picture"]}')

        for index, row in song_unique_dataset.iterrows():
            if row["song_name_artist_combined"] in list_of_products:
                pass
            else:
                # print(f'Index: {index}; Name: {row["song_name"]}; Artist: {row["song_artist"]}; ID: {row["song_name_artist_combined"]}; Picture: {row["song_picture"]}')
                p = Product(row["song_name"], row["song_artist"], row["song_picture"], row["song_name_artist_combined"])
                db.session.add(p)
                db.session.commit()

    return redirect(url_for('shop.home'))



