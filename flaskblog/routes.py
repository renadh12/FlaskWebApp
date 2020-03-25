from flask import render_template, url_for, flash, redirect, request
from flaskblog.models import User, Post
from flaskblog import app, bcrypt, db
from flaskblog.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required


# We have to set a secret key to our app protect it from modifying cookies, forgery attacks and cross site requests
# To generate a secret key
# Go to Terminal/Command line
# Type - python
# Type - import secrets
# Type - secrets.token_hex(16) - 16 is the number of bytes
# Copy the secret key and set it equal to app.config['SECRET_KEY']


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/fut')
def fut():
    return render_template('fut.html', title='FUT Blog')


@app.route('/about')
def about():
    return render_template('about.html', title='About Us')


@app.route('/register', methods=['GET', 'POST'])  # The methods will enable the site to accept HTTP requests for
# submission
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # hash password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # add all the user parameters
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # add the user to the database and commit
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been successfully created. You can log in now!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'You have successfully logged in!', 'success')
            next_page = request.args.get('next')  # retrieve the route parameter from the url query
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful! Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file)
