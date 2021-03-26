from app import db
from datetime import datetime as dt

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    song_name = db.Column(db.String)
    song_artist = db.Column(db.String)
    song_picture = db.Column(db.String)
    song_name_artist_combined = db.Column(db.String)
    price = db.Column(db.Float)
    tax = db.Column(db.Float)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    date_updated = db.Column(db.DateTime)


    def __init__(self, song_name, song_artist, song_picture, song_name_artist_combined):
        super().__init__()
        self.song_name = song_name.title()
        self.song_artist = song_artist.title()
        self.price = 0.99
        self.tax = 0.00
        self.song_picture = song_picture
        self.song_name_artist_combined = song_name_artist_combined

    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def to_dict(self):
    #     data = {
    #         'id': self.id,
    #         'song_name': self.song_name,
    #         'song_artist': self.song_artist,
    #         'song_picture': self.song_picture,
    #         'song_name_artist_combined': self.song_name_artist_combined,
    #         'price': 0.99,
    #         'tax': self.tax,
    #         'date_created': self.date_created,
    #         'date_updated': self.date_updated
    #     }
    #     return data

    # def from_dict(self, data):
    #     for field in ['song_name', 'song_artist', 'song_picture','song_name_artist_combined']:
    #         if field in data:
    #             setattr(self, field, data[field])
    #     setattr(self, 'tax', round(data[field] * 0.06),2)
    #     self.tax = round(self.price * 0.06,2)
 
    def __repr__(self):
        return f'<{self.song_name} by {self.song_artist}>'

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.ForeignKey('product.id'), nullable=False)
    date_added = db.Column(db.DateTime, default=dt.utcnow)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        from app.blueprints.auth.models import User
        return f'<Cart: {User.query.get({self.user_id}).email}: {Product.query.get(self.product_id).name}>'
