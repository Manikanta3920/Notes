from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime
import pytz

class Note(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    data=db.Column(db.String(100000))
    date = db.Column(db.DateTime, default=lambda: datetime.now(pytz.timezone('Asia/Kolkata')))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    firstName=db.Column(db.String(150))
    notes=db.relationship('Note')
