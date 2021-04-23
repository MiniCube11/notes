from flask import Blueprint, redirect, url_for, render_template
from flask_login import current_user

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    notes = current_user.notes.all()
    return render_template('main/index.html', notes=notes)
