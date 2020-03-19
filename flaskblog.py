from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# We have to set a secret key to our app protect it from modifying cookies, forgery attacks and cross site requests
# To generate a secret key
# Go to Terminal/Command line
# Type - python
# Type - import secrets
# Type - secrets.token_hex(16) - 16 is the number of bytes
# Copy the secret key and set it equal to app.config['SECRET_KEY']

app.config['SECRET_KEY'] = "c792f0e1522c28a04c94ac14e51e6647"


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/fut')
def fut():
    return render_template('fut.html', title='FUT Blog')


@app.route('/register', methods=['GET', 'POST'])  # The methods will enable the site to accept HTTP requests for
# submission
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account successfully created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
