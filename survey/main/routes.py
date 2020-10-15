from flask import render_template,request,Blueprint, redirect, url_for
from flask_login import login_user, current_user, logout_user , login_required
from survey.models import User


main = Blueprint('main', __name__)

@main.route("/home")
@login_required
def index():
    return render_template("index.html")






@main.route("/")
def landing():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    return render_template("landing.html")




