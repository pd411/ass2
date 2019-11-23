# coding: utf-8

from . import home
from flask import render_template, redirect, url_for, flash, session, request
from werkzeug.security import generate_password_hash
from .forms import LoginForm, RegisterForm
from app.models import User, Userlog
from app.models import db

@home.route("/")
def index():
    return render_template("home/index.html")


@home.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(username=data["username"]).first()
        if not user or not user.check_pwd(data["password"]):
            flash("Error password!", "err")
            return redirect(url_for("home.login"))
        session["user"] = user.username
        session["user_id"] = user.id
        userlog = Userlog(
            user_id=user.id,
            ip=request.remote_addr
        )
        db.session.add(userlog)
        db.session.commit()
        print(user)
        return redirect(url_for("home.index"))
    return render_template("home/login.html", form=form)

@home.context_processor
def my_context_processor():
    user = session.get('user')
    if user:
        return {'login_user': user}
    print(user)
    return {}

@home.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home.index"))


@home.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        user = User(
            username=data["username"],
            email=data["email"],
            pwd=generate_password_hash(data["password"])
        )
        db.session.add(user)
        db.session.commit()
        flash("success sign up!", "ok")
        session["user"] = user.username
        session["user_id"] = user.id
        return redirect(url_for("home.index"))
    return render_template("home/register.html", form=form)
