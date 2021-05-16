from app import app
from flask import request
import requests


def get_auth_url():
    auth_url = ["https://accounts.google.com/o/oauth2/v2/auth",
                "?scope=openid%20profile%20email",
                "&access_type=offline",
                "&include_granted_scopes=true",
                "&response_type=code",
                f"&redirect_uri={app.config['REDIRECT_URI']}/authorized",
                f"&client_id={app.config['GOOGLE_CLIENT_ID']}"
                ]
    return ''.join(auth_url)


def get_access_token():
    res = requests.post("https://oauth2.googleapis.com/token", json={
        "code": request.args.get("code"),
        "client_id": app.config['GOOGLE_CLIENT_ID'],
        "client_secret": app.config['GOOGLE_CLIENT_SECRET'],
        "grant_type": "authorization_code",
        "redirect_uri": f"{app.config['REDIRECT_URI']}/authorized"
    }).json()
    if 'error' in res:
        return 'error'
    return res['access_token']


def get_user_info(access_token):
    res = requests.post(
        "https://openidconnect.googleapis.com/v1/userinfo",
        headers={
            "Content-length": "0",
            "Content-type": "application/json",
            "Authorization": "Bearer " + access_token
        }
    ).json()
    return res
