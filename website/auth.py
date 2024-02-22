from flask import Blueprint, render_template, request, flash
#blueprint for flask app
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET']) # allows both send and receive requests and returns render_template
def login():
    return render_template("login.html",  boolean=True) # you can pass multiple variables, including text text="Testing"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters', category='error')
        else:
            flash('Account created!', category='success')
            
            
    return render_template("sign_up.html")