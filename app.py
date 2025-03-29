from flask import Flask, redirect, url_for
from models.user import db
from views.user import user_bp
from views.auth import auth_bp
from config import Config

def create_app():
    app = Flask(__name__)  # Create a Flask instance
    
    # Load configuration
    app.config.from_object(Config)
    
    # Initialize the database
    db.init_app(app)
    
    # Register Blueprints
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.config['SESSION_TYPE'] = 'filesystem'  # Store session in files
    
    # Root route redirects to login
    @app.route('/')
    def index():
        return redirect(url_for('auth_bp.login'))
    
    return app

if __name__ == "__main__":
    app = create_app()

    # Push application context before calling db.create_all()
    with app.app_context():
        db.create_all()

    app.run(debug=True)

