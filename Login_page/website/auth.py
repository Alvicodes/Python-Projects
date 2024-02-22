from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

#blueprint for flask app
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET']) # allows both send and receive requests and returns render_template
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
    
        user = User.query.filter_by(email=email).first() # filter all users with this email 'first' returns first result. SHould only bbe one
        if user: # If user found
            if check_password_hash(user.password, password):
                flash('Login successful!', category='success')
                login_user(user, remember=True) # remembers user whilst web server is running
                return redirect(url_for('views.home')) 
            else: 
                flash('Login failed!', category='error')
        else: # If user not found
            flash('Email does not exist!', category='error')    
        
    return render_template("login.html", user=current_user) # you can pass multiple variables, including text text="Testing"


@auth.route('/logout')
@login_required # makes it only accessible when logged in
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('User/Email already exists', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2')) # sha256 is a hashing algorithm 
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home')) # using views.home  t be redirected to the home page. Targets root incase of any change, no effect to code
            
    return render_template("sign_up.html", user=current_user)