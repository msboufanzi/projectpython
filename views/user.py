from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.user import User
from models.user import db

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/edit_user', methods=['POST'])
def edit_user():
    # Verifier si l'utilisateur est connecte
    if 'user_id' not in session:
        flash("Vous devez vous connecter d'abord.", "warning")
        return redirect(url_for('auth_bp.login'))

    # Recuperer les donnes du formulaire
    user_id = session.get('user_id')
    username = request.form.get('username')
    email = request.form.get('email')

    # Mettre a jour les information de l'utilisateur
    user = User.query.get(user_id)
    if user:
        user.username = username
        user.email = email
        db.session.commit()

        # Mettre a jour la session avec les nouvelles information
        session['username'] = username
        session['email'] = email
        flash('Informations mises à jour avec succès!', 'success')
    else:
        flash("Utilisateur non trouvé!", "danger")

    return redirect(url_for('user_bp.dashboard'))


@user_bp.route("/dashboard", methods=['GET'])
def dashboard():
    # Verifier si l'utilisateur est connecte
    if 'user_id' not in session:
        flash("Vous devez vous connecter d'abord.", "warning")
        return redirect(url_for('auth_bp.login'))

    # Preparer les information de l'utilisateur pour le template
    user_info = {
        "id": session.get("user_id"),
        "username": session.get("username"),
        "email": session.get("email"),
    }

    # Afficher le tableau de bord avec les information de l'utilisateur
    return render_template('manage_user.html', user=user_info)

