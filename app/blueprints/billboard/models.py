from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime as dt

class Song(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    song_name = db.Column(db.String)
    song_rank = db.Column(db.Integer)
    song_artist = db.Column(db.String)
    song_this_week = db.Column(db.String)
    song_last_week = db.Column(db.String)
    song_artist_peak_rank = db.Column(db.String)
    song_artist_weeks_on_chart = db.Column(db.String)
    song_picture = db.Column(db.String)
    start_of_week_date = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    song_name_artist_combined = db.Column(db.String)

    # def __init__(self, song_name, song_rank, song_artist, song_this_week, song_last_week, song_artist_peak_rank, song_artist_weeks_on_chart, song_picture, start_of_week_date, song_name_artist_combined):
    def __init__(self, song_name, song_rank, song_artist, song_picture, start_of_week_date, song_name_artist_combined):
        super().__init__()
        self.song_name = song_name.title()
        self.song_rank = song_rank
        self.song_artist = song_artist.title()
        # self.song_this_week = song_this_week
        # self.song_last_week = song_last_week
        # self.song_artist_peak_rank = song_artist_peak_rank
        # self.song_artist_weeks_on_chart = song_artist_weeks_on_chart
        self.song_picture = song_picture
        self.start_of_week_date = start_of_week_date
        self.song_name_artist_combined = song_name_artist_combined.lower()

    def __repr__(self):
        return f'<Song Name: {self.song_name} and Song Artist: {self.song_artist}>'


    def from_dict(self, data):
        for field in ['song_name','song_rank','song_artist','song_this_week','song_last_week','song_artist_peak_rank','song_artist_weeks_on_chart','song_picture','start_of_week_date', 'song_name_artist_combined']:
            if field in data:
                setattr(self, field, data[field])

    def unique_set_of_songs(self):
        from sqlalchemy import distinct, func
        unique_list_of_songs = select([func.distinct(Song.c.song_name_artist_combined)])
        return unique_list_of_songs
        # unique_list_of_songs = Song.query.join(
        #     followers,
        #     (followers.c.followed_id == Post.user_id)
        # ).filter(followers.c.follower_id == self.id)
        # self_posts = Post.query.filter_by(user_id=self.id)
        # all_posts = followed.union(self_posts).order_by(Post.date_created.desc())
        # return all_posts

        # for value in Session.query(Table.column).distinct():
        # pass