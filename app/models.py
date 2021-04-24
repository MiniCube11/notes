from app import db, login
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    user_caps = db.Column(db.String(64), index=True, unique=True)
    userid = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    is_admin = db.Column(db.Boolean, index=True)
    notes = db.relationship('Note', backref='author', lazy='dynamic')

    def set_valid_username(self, username):
        from random import randint
        user_caps = username.upper()
        existing_user = User.query.filter_by(user_caps=user_caps).first()
        if existing_user:
            username += '-'
            while existing_user:
                username = username + str(randint(0, 9))
                user_caps = username.upper()
                existing_user = User.query.filter_by(user_caps=user_caps).first()
        self.username = username
        self.user_caps = user_caps


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String, index=True, unique=True)
    title = db.Column(db.String(64), index=True)
    body = db.Column(db.String(2000), index=True)
    is_public = db.Column(db.Boolean, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def generate_key():
        LENGTH = 20
        chars = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
        chars2 = "-_1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
        s = ''
        from random import choice
        for i in range(LENGTH):
            if i == 0 or i == LENGTH:
                s += choice(chars)
            else:
                s += choice(chars2)
        return s

    def generate_valid_key(self):
        while True:
            key = self.generate_key()
            note = Note.query.filter_by(key=key).first()
            if not note:
                break
        return key

    def set_key(self):
        self.key = self.generate_valid_key()
