from flask import Blueprint, redirect, url_for, render_template
from flask_login import current_user
from app.models import Note

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    notes = Note.query.filter_by(author=current_user).order_by(Note.last_updated.desc()).all()
    return render_template('main/index.html', notes=notes)
