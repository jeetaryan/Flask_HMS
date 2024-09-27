# init.py

from flask import Flask
from app.extensions import db, jwt, login_manager
from app.config import Config
from app.routes.auth import auth_bp
from flask_migrate import Migrate

def create_app():
    app=Flask(__name__, template_folder='templates')
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt.init_app(app)
    login_manager.init_app(app)

    # Register mmodel
    from app.models.user import User
    from app import models
    # User loader function
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register routes
    app.register_blueprint(auth_bp)

    return app