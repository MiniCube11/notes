import os

if os.environ.get("TESTING"):
    REDIRECT_URI = "http://127.0.0.1:5000"
else:
    REDIRECT_URI = "https://notesapp0011.herokuapp.com"
SECRET_KEY = os.environ.get("SECRET_KEY")
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("://", "ql://", 1)
SQLALCHEMY_TRACK_MODIFICATIONS = False
ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")
