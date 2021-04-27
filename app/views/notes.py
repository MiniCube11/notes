from flask import Blueprint, redirect, render_template, url_for, request, abort, flash, session
from app import app, db
from app.models import Note
from flask_login import current_user, login_required
from datetime import datetime

bp = Blueprint('notes', __name__, url_prefix='/notes')


@bp.route('/new')
@login_required
def add_note():
    note = Note(title="Untitled", body='', author=current_user)
    note.set_key()
    db.session.add(note)
    db.session.commit()
    return redirect(url_for('notes.edit_note', key=note.key))


@bp.route('/<key>/edit', methods=['GET', 'POST'])
def edit_note(key):
    note = Note.query.filter_by(key=key).first_or_404()
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        note.title = title
        note.body = body
        note.last_updated = datetime.utcnow()
        db.session.commit()
    if note.author == current_user:
        return render_template('notes/edit_note.html', note=note)
    elif note.is_public:
        return render_template('notes/view_note.html', note=note)
    else:
        if current_user.is_authenticated:
            if current_user.is_admin:
                return render_template('notes/edit_note.html', note=note)
            else:
                abort(403)
        else:
            session['next'] = url_for('notes.edit_note', key=key)
            return redirect(url_for('auth.login'))


@bp.route('/<key>/delete', methods=['POST'])
def delete_note(key):
    note = Note.query.filter_by(key=key).first()
    flash(f"The note '{note.title}' has been deleted.")
    db.session.delete(note)
    db.session.commit()
    return "Done"


@bp.route('/<key>/public', methods=['POST'])
def toggle_public(key):
    note = Note.query.filter_by(key=key).first()
    if note.is_public:
        note.is_public = False
    else:
        note.is_public = True
    db.session.commit()
    return str(note.is_public)


@bp.route('/<key>/get', methods=['POST'])
def get_note(key):
    note = Note.query.filter_by(key=key).first()
    return {'title': note.title, 'body': note.body}
