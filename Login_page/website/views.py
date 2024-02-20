from flask import Blueprint, render_template
#blueprint for flask app
views = Blueprint('views', __name__)

@views.route('/') #decorator
def home():
    return render_template("home.html")