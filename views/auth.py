from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.user import User
from werkzeug.security import check_password_hash, generate_password_hash
from models.user import db

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.hashed_password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['email'] = user.email
            flash('Login successful!', 'success')
            return redirect(url_for('user_bp.dashboard'))
        
        flash('Invalid username or password', 'danger')  # Store error message
        return redirect(url_for('auth_bp.login'))
    
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('auth_bp.login'))


@auth_bp.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return render_template('signup.html', message={'error': 'Email already registered'})

        hashed_password = generate_password_hash(password)

        new_user = User(username=username, email=email, hashed_password=hashed_password)

        # Add user to the session
        db.session.add(new_user)
        db.session.commit()

        session['user_id'] = new_user.id
        session['username'] = new_user.username
        session['email'] = new_user.email

        flash('Account created successfully!', 'success')
        return redirect(url_for('user_bp.dashboard'))

    return render_template('signup.html')
