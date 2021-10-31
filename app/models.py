from datetime import datetime
from flask_login import UserMixin

from app import db, login_manager

# Define a User model
class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id            = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(128),  nullable=False)
    email    = db.Column(db.String(128),  nullable=False, unique=True)
    password = db.Column(db.String(192),  nullable=False)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<role %r>' % self.name

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

