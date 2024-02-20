from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'iansn3AJ08na2n0J'
    
    #registering blueprints with views/urls for app and location
    from.views import views
    from.auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') # using only slash here as we dont want anything else in the prefix, keep it simple
    
    return app