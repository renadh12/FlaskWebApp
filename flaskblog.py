from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# We have to set a secret key to our app protect it from modifying cookies, forgery attacks and cross site requests
# To generate a secret key
# Go to Terminal/Command line
# Type - python
# Type - import secrets
# Type - secrets.token_hex(16) - 16 is the number of bytes
# Copy the secret key and set it equal to app.config['SECRET_KEY']

app.config['SECRET_KEY'] = "c792f0e1522c28a04c94ac14e51e6647"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"  # three forward slashes for relative path to the current
# directory
db = SQLAlchemy(app)  # Set up db instance


# Create tables and columns

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(60), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)  # the password is going to be hashed which will
    # generate a 60 character long hashing key

    # linking users with each post. Backref will add the
    # author column, lazy set to true will load the data in one go
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}' , '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)

    # we are passing utcnow as an argument and not as a function
    # utcnow() because we don't want to pass the
    # current date as an argument. The function will run after it's passed along
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    # Linking Post table to User table using FK user.id. Since we are referencing the User table
    # we are using lowercase "user"
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}' , '{self.date_posted}')"


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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account successfully created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "renc17@gmail.co" and form.password.data == 'password':
            flash(f'You have successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password!', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
