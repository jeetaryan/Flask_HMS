from flask_login import login_user
from app.models.user import User
from app.extensions import db

def login_user_service(username, password):
    try:
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return user
    except Exception as e:
        return None
    return None

def register_user_service(username, password, email):
    try:
        user = User.query.filter_by(username=username).first()
        if user:
            return None
        else:
            hash_pass = User.hash_password(password)
            new_user = User(username, hash_pass, email)
            db.session.add(new_user)
            db.session.commit()
            return new_user
    except Exception as e:
        db.session.rollback()  # Roll back any changes on error
        return None
    finally:
        db.session.close()  # Ensure the session is closed