from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from sqlalchemy.exc import IntegrityError

auth = Blueprint('auth', __name__)


@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    user_name = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    password2 = request.form.get('confirm_password')
    phone_number = request.form.get('phone_number')

    try:
        if user_name == 'root':
            flash('Invalid username', category='error')
        elif len(str(password)) < 6:
            flash('Password must be at least 6 characters long', category='error')
        elif password != password2:
            flash('Passwords do not match', category='error')
        elif len(email) < 4:
            flash('Email must be at least 4 characters long', category='error')
        else:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(user_name=user_name, email=email, password=hashed_password, phone_number=phone_number)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', category='success')

    except IntegrityError as e:
        db.session.rollback()  # Roll back the session to prevent partial changes
        flash('An error occurred while creating the account. Please try again later.', category='error')

    return render_template("signup.html")



@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')