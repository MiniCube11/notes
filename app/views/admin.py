from flask import Blueprint, render_template, abort, request
from app.models import User, Note
from flask_login import current_user, login_required

bp = Blueprint('admin', __name__, url_prefix="/admin")


@bp.route('/')
@login_required
def admin_home():
    if not current_user.is_admin:
        abort(403)
    return render_template('admin/index.html')


@bp.route('/users')
@login_required
def users():
    if not current_user.is_admin:
        abort(403)
    notes = False
    if request.args.get('notes'):
        notes = True
    return render_template('admin/users.html', users=User.query.order_by(User.id).all(), notes=notes)


@bp.route('/notes')
@login_required
def notes():
    if not current_user.is_admin:
        abort(403)
    return render_template('admin/notes.html', notes=Note.query.all())
