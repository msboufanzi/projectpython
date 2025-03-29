from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.user import User
from werkzeug.security import check_password_hash, generate_password_hash
from models.user import db

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    # Verifier si la methode est POST pour traiter le formulaire
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Chercher l'utilisateur dans la base de donnes
        user = User.query.filter_by(username=username).first()

        # Verifier si l'utilisateur existe et le mot de passe est correct
        if user and check_password_hash(user.hashed_password, password):
            # Stocker les information de l'utilisateur dans la session
            session['user_id'] = user.id
            session['username'] = user.username
            session['email'] = user.email
            flash('Connexion réussie!', 'success')
            return redirect(url_for('user_bp.dashboard'))
        
        # Si les information sont incorrect, afficher un message d'erreur
        flash('Nom d\'utilisateur ou mot de passe invalide', 'danger')
        return redirect(url_for('auth_bp.login'))
    
    # Si la methode est GET, afficher la page de connexion
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    # Effacer la session et rediriger vers la page de connexion
    session.clear()
    flash('Déconnexion réussie!', 'success')
    return redirect(url_for('auth_bp.login'))


@auth_bp.route('/signup', methods=['POST', 'GET'])
def signup():
    # Verifier si la methode est POST pour traiter le formulaire d'inscription
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Verifier si l'email existe deja
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return render_template('signup.html', message={'error': 'Cet email est déjà utilisé'})

        # Hasher le mot de passe pour la securite
        hashed_password = generate_password_hash(password)

        # Creer un nouvel utilisateur
        new_user = User(username=username, email=email, hashed_password=hashed_password)

        # Ajouter l'utilisateur a la base de donnes
        db.session.add(new_user)
        db.session.commit()

        # Connecter l'utilisateur automatiquement apres l'inscription
        session['user_id'] = new_user.id
        session['username'] = new_user.username
        session['email'] = new_user.email

        flash('Compte créé avec succès!', 'success')
        return redirect(url_for('user_bp.dashboard'))

    # Si la methode est GET, afficher la page d'inscription
    return render_template('signup.html')

