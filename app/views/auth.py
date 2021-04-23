from flask import Blueprint, redirect, render_template, url_for, session
from werkzeug.urls import url_parse
from app import db
from app.oauth import get_auth_url, get_access_token, get_user_info
from app.models import User
from flask_login import current_user, login_user, logout_user

bp = Blueprint('auth', __name__)


@bp.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    return render_template('auth/login.html')


@bp.route('/auth/google')
def authorize():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    return redirect(get_auth_url())


@bp.route('/authorized')
def authorized():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    access_token = get_access_token()
    user_info = get_user_info(access_token)
    user = User.query.filter_by(userid=user_info['sub']).first()
    if user:
        login_user(user, remember=True)
        next_page = session.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        session.pop('next', None)
        return redirect(next_page)

    user = User(userid=user_info['sub'], email=user_info['email'])
    username = user_info['email'].split('@')[0]
    user.set_valid_username(username)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return redirect(url_for('main.index'))


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
