import os

REDIRECT_URI = os.environ.get('REDIRECT_URI')
SECRET_KEY = os.environ.get("SECRET_KEY")
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("postgres://", "postgresql://", 1)
SQLALCHEMY_TRACK_MODIFICATIONS = False
ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")
