from flask import Flask, redirect, url_for
from models.user import db
from views.user import user_bp
from views.auth import auth_bp
from config import Config

def create_app():
    app = Flask(__name__)  # Create a Flask instance
    
    # Charger la configuration
    app.config.from_object(Config)
    
    # Initialiser la base de donnes
    db.init_app(app)
    
    # Enregistrer les Blueprints
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.config['SESSION_TYPE'] = 'filesystem'  # Stocker les session dans des fichiers
    
    # Route principal rediriger vers login
    @app.route('/')
    def index():
        return redirect(url_for('auth_bp.login'))
    
    return app

if __name__ == "__main__":
    app = create_app()

    # Pousser le contexte d'application avant d'appeler db.create_all()
    with app.app_context():
        db.create_all()

    app.run(debug=True)

