from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_required, current_user
from app import db
from app.models import User
from re import match

bp = Blueprint('account', __name__)


@bp.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    if request.method == 'POST':
        username = request.form['username']
        valid = match("^(?=.{3,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$", username)
        user_caps = username.upper()
        if current_user.username == username or current_user.user_caps == user_caps:
            return redirect(url_for('account.account'))
        elif User.query.filter_by(user_caps=user_caps).first():
            flash(f"The username '{username}' is already taken.", "error")
            return redirect(url_for('account.account'))
        elif not valid:
            flash("Please enter a valid username.", "error")
            return redirect(url_for('account.account'))
        else:
            flash("Your username has been changed successfully.")
            current_user.username = username
            current_user.user_caps = user_caps
            db.session.commit()
        return redirect(url_for('account.account'))
    return render_template("account/account.html", form_title="Account", form_button="Save")
