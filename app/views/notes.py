from flask import Blueprint, redirect, render_template, url_for, request, abort, flash, session
from app import db
from app.models import Note
from flask_login import current_user, login_required
from datetime import datetime

bp = Blueprint('notes', __name__, url_prefix='/notes')


def create_note():
    note = Note(title="Untitled", body='', author=current_user)
    note.set_key()
    db.session.add(note)
    db.session.commit()
    return note.key


def update_note(note):
    title = request.form.get("title")
    body = request.form.get("body")
    note.last_updated = datetime.utcnow()
    db.session.commit()
    try:
        note.title = title
        db.session.commit()
    except:
        return "Title is too long (maximum 64 characters)"
    try:
        note.body = body
        db.session.commit()
    except:
        return "Text is too long (maximum 2000 characters)"
    return "done"


def delete_note(note):
    flash(f"The note '{note.title}' has been deleted.")
    db.session.delete(note)
    db.session.commit()


@bp.route('/new')
@login_required
def new():
    note_key = create_note()
    return redirect(url_for('notes.get_note', key=note_key))


@bp.route('/<key>/edit')
def old_edit_note(key):
    return redirect(url_for('notes.edit_note', key=key))


@bp.route('/api/<key>', methods=['GET', 'POST', 'DELETE'])
def edit_note(key):
    note = Note.query.filter_by(key=key).first_or_404()
    if request.method == "GET":
        return {'title': note.title, 'body': note.body}
    allowed = False
    if note.is_public:
        allowed = True
    if current_user.is_authenticated:
        if current_user.is_admin or note.author == current_user:
            allowed = True
    if not allowed:
        if not current_user.is_authenticated:
            return "Unauthorized", 401
        else:
            return "Forbidden", 403
    if request.method == "POST":
        return update_note(note)
    elif request.method == "DELETE":
        delete_note(note)
        return "done"


@bp.route('/<key>/public', methods=['POST'])
def toggle_public(key):
    note = Note.query.filter_by(key=key).first()
    if note.is_public:
        note.is_public = False
    else:
        note.is_public = True
    db.session.commit()
    return str(note.is_public)


@bp.route('/<key>')
def get_note(key):
    note = Note.query.filter_by(key=key).first_or_404()
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


@bp.route('/<key>/update')
def update_content(key):
    note = Note.query.filter_by(key=key).first_or_404()
    return {"title": note.title, "body": note.body}
