from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
class Note(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  data=db.Column(db.string(10000))
  date=db.Column(db.DateTime(timezone=True),default=func.now())
  user_id=db.Column(db.Integer.db.ForeignKey('user.id'))

class User(db.Model,UserMixin):
  id = db.Column(db.Integer,primary_key=True)
  email = db.Column(db.string(150),unique=True)
  password = db.Column(db.string(150))
  firstname = db.Column(db.string(150))
  notes =db.relationship('Note')#same as Note calss name