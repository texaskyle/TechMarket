from market import app
from flask import render_template, request, redirect, url_for, flash
from market.models import Stock, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user, logout_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')


@app.route('/market')
def market_page():
    stock = Stock.query.all()
    return render_template('market.html', stock=stock)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    # checking the errors in the form.errors dictionary
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error while creating a user {err_msg}", category='danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash(f"You have been logout", category='info')
    return redirect(url_for('home_page'))