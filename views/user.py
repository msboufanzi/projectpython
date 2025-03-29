from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.user import User
from models.user import db

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/edit_user', methods=['POST'])
def edit_user():
    if 'user_id' not in session:
        flash("You need to log in first.", "warning")
        return redirect(url_for('auth_bp.login'))

    user_id = session.get('user_id')
    username = request.form.get('username')
    email = request.form.get('email')

    user = User.query.get(user_id)
    if user:
        user.username = username
        user.email = email
        db.session.commit()

        session['username'] = username
        session['email'] = email
        flash('User information updated successfully!', 'success')
    else:
        flash("User not found!", "danger")

    return redirect(url_for('user_bp.dashboard'))


@user_bp.route("/dashboard", methods=['GET'])
def dashboard():
    if 'user_id' not in session:
        flash("You need to log in first.", "warning")
        return redirect(url_for('auth_bp.login'))  # Use auth_bp for login

    user_info = {
        "id": session.get("user_id"),
        "username": session.get("username"),
        "email": session.get("email"),
    }

    return render_template('manage_user.html', user=user_info)
