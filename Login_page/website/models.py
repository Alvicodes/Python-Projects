from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func #func gets the current date and time

# Setting up classes to store data you want from the website. Below is one to many

class Note(db.Model):#all notes need to conform to the below parameters
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #linking different information between users aka foreign keys. capitals for class in py but in sql doesn't matter hence user.id
    

class User(db.Model, UserMixin): #all users need to conform to the below parameters
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # relationship HERE NEEDS capital as it's referencing a CLASS DAW