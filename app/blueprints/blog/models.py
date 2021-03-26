from app import db
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    date_created = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    date_updated = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f'<Post: {self.id} - ID: {self.body}>'

