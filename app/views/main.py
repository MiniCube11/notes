from flask import Blueprint, redirect, url_for, render_template
from flask_login import current_user
from app.models import Note
from app import app, db

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    if current_user.email == app.config['ADMIN_EMAIL']:
        current_user.is_admin = True
        db.session.commit()
    notes = Note.query.filter_by(author=current_user).order_by(Note.last_updated.desc()).all()
    return render_template('main/index.html', notes=notes)
