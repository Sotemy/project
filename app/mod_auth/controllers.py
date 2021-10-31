from flask import request, render_template, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, current_user, logout_user
from werkzeug.urls import url_parse
# Import the database object from the main app module
from app import db

# Import module forms
from app.mod_auth.forms import LoginForm, RegisterForm

# Import module models (i.e. User)
from app.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
from app.mod_auth import mod_auth

# Set the route and accepted methods
@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('site. index'))
    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):

            login_user(user, remember=form.remember_me.data)
            flash('Welcome %s' % user.name)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('site.index')
            return redirect(next_page)
        else:
            flash('Wrong email or password', 'error-message')

    return render_template("auth/signin.html", form=form)

@mod_auth.route('/register/', methods=['GET', 'POST'])
def register():

    # If sign in form is submitted
    form = RegisterForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user:
            return flash('User %s exists' % user.name)
        else:
            hashpwd=generate_password_hash(form.password.data)
            user=User(name=form.name.data, email=form.email.data, password=hashpwd)
            try:
                db.session.add(user)
                db.session.commit()
            except Exception as error:
                return f'error:{error}'

        return redirect(url_for('auth.signin'))

    return render_template("auth/register.html", form=form)

@mod_auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))