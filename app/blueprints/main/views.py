from app import db
from flask import render_template, request, redirect, url_for, flash, session
from app.blueprints.auth.models import User
# from app.blueprints.auth.models import Followers
from app.blueprints.blog.models import Post
from app.blueprints.billboard.models import Song
from app.blueprints.shop.models import Product
from flask_login import login_user, current_user, logout_user, login_required
from .import bp as main_bp
from datetime import datetime
import os
from dotenv import load_dotenv

import numpy as np
import pandas as pd
import sqlalchemy

@main_bp.route('/test')
def test():
    labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
    ]

    values = [
        967.67, 1190.89, 1079.75, 1349.19,
        2328.91, 2504.28, 2873.83, 4764.87,
        4349.29, 6458.30, 9907, 16297
    ]

    colors = [
        "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
        "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
        "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

    bar_labels=labels
    bar_values=values
    return render_template('test.html', title='Bitcoin Monthly Price in USD', max=400, labels=bar_labels, values=bar_values)

    # return render_template('test.html')

@main_bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@main_bp.route('/home_testing')
def home():
    return render_template('home_v2.html')

@main_bp.route('/')
def home_testing():
    return render_template('home.html')


@main_bp.route('/general')
@login_required
def general():
    if current_user.is_authenticated:
        posts = current_user.followed_posts().all()
    else:
        posts = []
    context = {
        'user': current_user,
        'users': [user for user in User.query.all() if current_user.id != user.id],
        'posts': posts
    }
    return render_template('general.html', **context)


@main_bp.route('/profile')
@login_required
def profile():

    id = current_user.id
    user = User.query.get_or_404(id)
    print(f'Printing off the user object: {user}')
    print(f'Printing off the user id: {user.id}')

    all_followed_people = user.followed.all()
    print(f'Printing off the people this person is following: {all_followed_people}')
    all_followed_people_count = len(all_followed_people)
    print(f'Printing off the count of people this person is following: {all_followed_people_count}')

    all_following_me = user.following_me(id)
    print(f'Printing off the people following me: {all_following_me}')
    # print(f'Printing off the people following me: {all_following_me} and the type is: {type(all_following_me)}')
    # all_following_me_count = len(list(all_following_me))
    # print(f'Printing off the count of people followin me: {all_following_me_count}')

    context = {
        'user': current_user,
        'all_users': [user for user in User.query.all() if current_user.id != user.id],
        'total_followed_user_count': all_followed_people,
        'total_following_me_user_count': all_following_me,
        'posts': [p for p in Post.query.order_by(Post.date_created.desc()).all() if p.user_id == current_user.id]
    }
    return render_template('profile.html', **context)


@main_bp.route('/your_library')
def your_library():
    context = {
        'products': Product.query.all()
    }
    return render_template('your_library.html', **context)


@main_bp.route('/data_creation', methods=['GET', 'POST'])
def data_creation():
    engine = sqlalchemy.create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'))
    sql_song_data = pd.read_sql_table('song',engine)
    sql_product_data = pd.read_sql_table('product',engine)

    print("-"*100)
    songs_count = len(sql_song_data)
    min_date_songs = sql_song_data['start_of_week_date'].min()
    max_date_songs = sql_song_data['start_of_week_date'].max()

    product_count = len(sql_product_data)
    print(f'Total counts of song data: {songs_count}')
    print(f'Min date song data: {min_date_songs}')
    print(f'Max date of song data: {max_date_songs}')

    print()
    print(f'Total counts of product data: {product_count}')
    print("-"*100)

    context = {
        'songs_in_song_database': songs_count,
        'min_song_date': min_date_songs,
        'max_song_date': max_date_songs,
        'products_in_product_database': product_count
    }
    return render_template('data_creation.html' , **context)



@main_bp.route('/analysis', methods=['GET', 'POST'])
def analysis():
    context = {
    }
    decade_list = []
    now_time = datetime.now()
    now_year = now_time.year
    print(f'This is the now time: {now_time} and this is the year {now_year}')

    # for x in range(1950,now_year+10,10):
    #     decade_list.append(x)
    # print("+"*100)
    # print(f'This is the decade list: {decade_list}')
    # print("+"*100)

    # for x in range(1950,now_year+10,10):
    #     range(1950,now_year+10,10):
    #         print(f'this is x: {x} and this is y: {y}')

    # decade_list = []
    # start_of_decade = 1950
    # for year in range(start_of_decade,now_year,10):
    #     decade_dict = {}
    #     if year % 10 == 0:
    #         decade = year

    #         # decade_list.append(decade)
    #         decade_dict[decade] = year
    #         print(decade)

    #         # decade_list.append(decade_dict)
    # print("+"*100)
    # print(f'this is the decade list: {decade_list}')
    # print(f'this is the decade dictionary: {decade_dict}')
    # print("+"*100)


    # if request.method == 'POST':
    #     try:
    #         decade_inquiry = request.form['song_decade_search']
    #         if decade_inquiry not in decade_list:
    #             flash('Sorry that decade is not in the list of searchable queries. Please try again.', 'danger')
    #         else:
    #             song_data = Song.query.filter_by(song_name=decade_inquiry).first()
    #             song_dict = {"name": song_data} 
    #             context['songs'] = decade_inquiry

    #             print(f'This is what the person typed in: {decade_inquiry}')
    #             print(f'This is the song data: {song_data}')
    #             print(f'This is the song name: {song_data.song_name}')
    #             print(f'This is the song rank: {song_data.song_rank}')
    #             print(f'This is the song dict: {song_dict}')
    #             print(f'This is the context processor: {context}')

    #             return redirect(url_for('main.analysis_results', song_data=decade_inquiry, **request.args))
    #     except:
    #         flash('There was an error pull information about your song. Please check the spelling and try again.', 'danger')
    #         return redirect(url_for('main.analysis'))
    #     return redirect(url_for('main.analysis_results'))
    return render_template('analysis.html' , **context)


@main_bp.route('/analysis/results', methods=['GET', 'POST'])
def analysis_results():
    return render_template('analysis_results.html')





@main_bp.route('/analysis/results/test', methods=['GET', 'POST'])
def testing():
    # https://www.sqlshack.com/exploring-databases-in-python-using-pandas/
    engine = sqlalchemy.create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'))
    sql_data = pd.read_sql_table('song',engine)

    sql_song_specific_query = sql_data[(sql_data.song_name == "Patricia")]
    print(f'CHECK THIS OUT: {sql_song_specific_query}')
    keeping_songs_line_graph = sql_song_specific_query[['start_of_week_date','song_rank']]
    print(f'CHECK THIS OUT AGAIN: {keeping_songs_line_graph}')

    line_labels=pd.Series(keeping_songs_line_graph['start_of_week_date'])
    line_values=pd.Series(keeping_songs_line_graph['song_rank'])
    return render_template('test2.html', title='Chart Top 100 History for ', max=100, labels=line_labels, values=line_values)



@main_bp.route('/explore', methods=['GET', 'POST'])
@login_required
def explore():
    song_inquiry = ''

    from  sqlalchemy.sql.expression import func
    top_10_song_random = Product.query.order_by(func.random()).limit(10).all()
    print("-"*100)
    print(f'This is the top 10 random songs {top_10_song_random}')
    print("-"*100)


    context = {
        # 'products': Song.query.all(),
        # 'products': Song.query.limit(10),
        'products': top_10_song_random,
        'users': [user for user in User.query.all() if current_user.id != user.id],
        'songs': song_inquiry
    }

    if request.method == 'POST':
        try:
            song_inquiry = request.form['song_search']
            song_inquiry = song_inquiry.title()
            song_data = Song.query.filter_by(song_name=song_inquiry).first()
            # song_data = [song for song in Song.query.all() if song.song_name == song_inquiry]
            song_dict = {"name": song_data} 
            # session['song_data'] = song_dict

            context['songs'] = song_inquiry

            print(f'This is what the person typed in: {song_inquiry}')
            print(f'This is the song data: {song_data}')
            print(f'This is the song name: {song_data.song_name}')
            print(f'This is the song rank: {song_data.song_rank}')
            print(f'This is the song dict: {song_dict}')
            print(f'This is the context processor: {context}')

            return redirect(url_for('main.explore_results', song_data=song_inquiry, **request.args))
        except:
            flash('There was an error pull information about your song. Please check the spelling and try again.', 'danger')
            return redirect(url_for('main.explore'))
        return redirect(url_for('main.explore_results'))
    return render_template('explore.html', **context)

@main_bp.route('/explore/results', methods=['GET', 'POST'])
@login_required
def explore_results():
    # https://www.sqlshack.com/exploring-databases-in-python-using-pandas/
    engine = sqlalchemy.create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'))
    sql_data = pd.read_sql_table('song',engine)

    data_pull = request.args.get("song_data")
    song_name_selection = Song.query.filter_by(song_name=data_pull).order_by(Song.start_of_week_date.desc()).first()
    song_artist_selection = song_name_selection.song_artist
    song_artist_selection_final = song_name_selection.song_name

    print("_"*100)
    print(f'THE SONG ARTIST IS: {song_artist_selection} and SONG NAME: {song_artist_selection_final}')
    print("_"*100)

    # BAR GRAPH ---------------------------------------------------------------------
    sql_artist_query = sql_data[(sql_data.song_artist == song_artist_selection)]
    keeping_songs = sql_artist_query
    print("+"*100)
    print(keeping_songs)
    print("+"*100)
    song_counts = keeping_songs.song_name.value_counts()[0:10]
    print("-"*100)
    print(f'THE SONG COUNT IS: {song_counts}')
    print("-"*100)
    max_keeping_songs = keeping_songs.song_name.value_counts().max()
    print("="*100)
    print(f'THE SONG MAX IS: {max_keeping_songs}')
    print("="*100)

    if max_keeping_songs <=5:
        max_lab_bar = 10
    elif max_keeping_songs <=10:
        max_lab_bar = 15
    elif max_keeping_songs <=15:
        max_lab_bar = 20
    elif max_keeping_songs <=20:
        max_lab_bar = 30
    elif max_keeping_songs <=30:
        max_lab_bar = 40
    elif max_keeping_songs <=40:
        max_lab_bar = 50
    elif max_keeping_songs <=50:
        max_lab_bar = 100
    elif max_keeping_songs <=100:
        max_lab_bar = 200
    elif max_keeping_songs <=200:
        max_lab_bar = 500
    else:
        max_lab_bar = 1000

    song_bands = song_counts
    labels = song_bands.index
    values = song_bands.values
    bar_labels=labels
    print("+"*100)
    print(bar_labels)
    print("+"*100)
    bar_values=values
    print("-"*100)
    print(bar_values)
    print("-"*100)





    # LINE GRAPH ---------------------------------------------------------------------
    sql_song_specific_query = sql_data[(sql_data.song_name == song_artist_selection_final)]
    keeping_songs_line_graph = sql_song_specific_query[['start_of_week_date','song_rank']]
    line_labels=pd.Series(keeping_songs_line_graph['start_of_week_date'])
    line_values=pd.Series(keeping_songs_line_graph['song_rank'])



    # data = request.args.get("song_data", type=dict)
    data = request.args.get("song_data")
    # print(f'CHECK MEEEEEEE1: {data}')

    context = {
    'users': [user for user in User.query.all() if current_user.id != user.id],
    'songs': [song for song in Song.query.order_by(Song.start_of_week_date.desc()).all()  if song.song_name == data],
    'songs_latest_date': Song.query.filter_by(song_name=data).order_by(Song.start_of_week_date.desc()).first()
    }
    if request.method == 'GET':
        # print(f'This is the UPDATED context processor: {context}')
        # return render_template('explore_results.html', **context)
        return render_template('explore_results.html', title=f'{song_artist_selection} Best 10 Songs in Top 100 Billboard', max=max_lab_bar, labels=bar_labels, values=bar_values, title_line=f'{song_artist_selection_final} - History on the Charts', max_line=100, labels_line=line_labels, values_line=line_values, **context)


