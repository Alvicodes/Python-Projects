from flask import Blueprint, render_template
#blueprint for flask app
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html",  boolean=True) # you can pass multiple variables, including text text="Testing"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")