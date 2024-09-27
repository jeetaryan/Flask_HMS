# auth.py

from flask import Blueprint, render_template, url_for, redirect, request
from app.forms.login_form import LoginForm
from app.services.auth_service import login_user_service

auth_bp = Blueprint('auth', __name__)


@auth_bp.route("/", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if request.method =="POST":
        if login_form.validate_on_submit():
            user = login_user_service(login_form.username.data,login_form.password.data)
            if user:
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login',error_message='invalid credential.'))
        else:
            return redirect(url_for('login'))
    else:
        return render_template('auth/login.html', form=login_form)