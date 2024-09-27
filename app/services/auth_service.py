# auth_service.py

from flask_login import login_user
from app.models.user import User


def login_user_service(username, password):
    user = User.query.filter_by(username=username).first()
    if user and User.check_password(password):
        login_user(user)
        return user
    return None
