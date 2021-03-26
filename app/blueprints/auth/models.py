from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
import shortuuid
from app.blueprints.blog.models import Post
from hashlib import md5
from datetime import datetime 

# Using sqlalchemy to create a table instead of creating it using flask like we did below
followers = db.Table(
    'followers', 
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id')),
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True, default=None)
    password = db.Column(db.String)
    posts = db.relationship('Post', cascade='all, delete-orphan', backref='user', lazy=True)
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('follwers', lazy='dynamic'),
        lazy='dynamic'
    )
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)


    # following_me = db.relationship(
    #     'User', secondary=followers,
    #     primaryjoin=(followers.c.follower_id == id),
    #     backref=db.backref('follwers', lazy='dynamic'),
    #     lazy='dynamic'
    # )


    # following_me = db.relationship(
    #     'User', secondary=followers,
    #     primaryjoin=(followers.c.follower_id == id),
    #     secondaryjoin=(followers.c.followed_id != id),
    #     backref=db.backref('follwers', lazy='dynamic'),
    #     lazy='dynamic'
    # )

    # following_me_again = db.relationship(
    #     'User', secondary=followers,
    #     primaryjoin=(followers.c.follower_id != id),
    #     secondaryjoin=(followers.c.followed_id != id),
    #     backref=db.backref('follwers', lazy='dynamic'),
    #     lazy='dynamic'
    # )

    # following_me_thrice = db.relationship(
    #     'User', secondary=followers,
    #     primaryjoin=(followers.c.follower_id != id),
    #     secondaryjoin=(followers.c.followed_id == id),
    #     backref=db.backref('follwers', lazy='dynamic'),
    #     lazy='dynamic'
    # )

    cart = db.relationship('Cart', cascade='all, delete-orphan', backref='user', lazy=True)

    def __init__(self, first_name, last_name, password):
        super().__init__()
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.password = password
        self.email = f'{first_name}{last_name[0]}@codingtemple.com'.lower()

    def followed_posts(self):
        followed = Post.query.join(
            followers,
            (followers.c.followed_id == Post.user_id)
        ).filter(followers.c.follower_id == self.id)
        self_posts = Post.query.filter_by(user_id=self.id)
        all_posts = followed.union(self_posts).order_by(Post.date_created.desc())
        return all_posts

    def following_me(self, id):
        people_following_me = User.query.join(
            followers,
            (followers.c.followed_id == User.id)
        ).filter(followers.c.followed_id == self.id)
        people_following_me_num = people_following_me.count()
        print(f'this is the method print {people_following_me_num}')
        return people_following_me_num

    def avatar(self, email, size):
        digest = md5(email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
            db.session.commit()

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
            db.session.commit()

    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def create_password_hash(self, password):
        self.password = generate_password_hash(password)

    def verify_password_hash(self, password_to_verify):
        return check_password_hash(self.password, password_to_verify)

    def save(self):
        self.create_password_hash(self.password)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<User: {self.email}>'

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)
