from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'iansn3AJ08na2n0J'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    
    #registering blueprints with views/urls for app and location
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') # using only slash here as we dont want anything else in the prefix, keep it simple
    
    from .models import User, Note
    create_database(app)
    
    return app

# create function to check if database already exists
def create_database(app):
    if not path.exists('website/' + DB_NAME): # using a path module to check if db exists
        with app.app_context():
            db.create_all() # create db if it doesn't exist
        print('Created Database!')
