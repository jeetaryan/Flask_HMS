# auth.py

from flask import Blueprint, render_template, url_for, redirect, request, flash, jsonify
from app.forms.login_form import LoginForm, RegisterForm
from app.services.auth_service import login_user_service, register_user_service

auth_bp = Blueprint('auth', __name__)


@auth_bp.route("/", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if request.method == "POST":
        if login_form.validate_on_submit():
            user = login_user_service(login_form.username.data, login_form.password.data)
            if user:
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login', error_message='invalid credential.'))
        else:
            return redirect(url_for('login'))
    else:
        return render_template('auth/login.html', form=login_form)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        data = request.get_json()
        register_form = RegisterForm(data=data)
        if register_form.validate():
            try:
                user = register_user_service(
                    register_form.username.data,
                    register_form.password.data,
                    register_form.email.data
                )
                if user:
                    return jsonify(success=True, message='Registration successful! Please log in.'), 201
                else:
                    return jsonify(success=False, message='Username already exists. Please choose a different one.'), 409
            except Exception as e:
                return jsonify(success=False, message='An error occurred during registration. Please try again.'), 500
        else:
            return jsonify(success=False, message='Form validation failed. Please check your inputs.', errors=register_form.errors), 400
    else:
        register_form = RegisterForm()
        return render_template('auth/register.html', form=register_form)