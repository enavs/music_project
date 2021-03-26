from .import bp as blog_bp
from flask import request, flash, redirect, url_for, render_template, session
# from .models import Post
from app.blueprints.blog.models import Post

from app import db
from flask_login import current_user, login_user, login_required
# from app.blueprints.auth.models import User
from .import bp as main_bp


@blog_bp.route('/post/create', methods=['POST'])
@login_required
def create_post():
    if request.method == 'POST':
        try:
            data = request.form['status_update']
            p = Post(body=data, user_id=current_user.id)
            print(p.__dict__)
            db.session.add(p)
            db.session.commit()
            flash('Post was created successfully', 'info')
        except:
            flash('There was an error creating your post. Try again.', 'danger')
    return redirect(url_for('main.general'))


@blog_bp.route('/posts/<int:post_id>', methods=['GET', 'POST'])
@login_required
def post_edit(post_id):
    posting_id = int(post_id)
    # print(f'this is the CHECKKKKKKKKKKKKK post: {posting_id}')
    post = Post.query.get_or_404(post_id)
    # print(f'this is the check post: {post}')

    context = {
    # 'posts': [p for p in Post.query.order_by(Post.date_created.desc()).all() ]
    # 'posts': [p for p in current_user.followed_posts().all() ]
    'post': post
    }
    return render_template('post_edit.html', **context)

    

@blog_bp.route('/post/delete/<int:post_id>', methods=['GET'])
@login_required
def post_delete(post_id):
    post = Post.query.get_or_404(post_id)
    # print(f'printed stuff GOOOOOOOOO {post}')
    db.session.delete(post)
    db.session.commit()
    flash("Post has been deleted successfully", 'success')
    return redirect(url_for('main.general'))


@blog_bp.route('/post/update/<int:post_id>', methods = ['GET', 'POST'])
@login_required
def post_update(post_id):
    if request.method == 'POST':
        post = Post.query.get_or_404(post_id)
        # print(f'post is: {post}')
        form = request.form
        # print(f'THIS IS the form: {form}')
        post.body = form['status_change_post']
        # print(f'form is: {form}, text is: {post.body}')
        db.session.commit()
        flash("Post has been updated successfully", 'success')
        return redirect(url_for('main.general'))



@blog_bp.route('/post/editing/<int:post_id>', methods=['GET', 'POST'])
@login_required
def post_edit_test(post_id):
    return render_template('post_edit_2.html')
