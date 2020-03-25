from flask_wtf import FlaskForm  #
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms import StringField, PasswordField, SubmitField, \
    BooleanField  # Import stringfield class to write the fields for
from flaskblog.models import User


# user_inputs - username email


class RegistrationForm(FlaskForm):  # RegistrationForm will inherit from FlaskForm class

    # To limit a user from entering invalid data - leaving the field blank, entering more than 50 characters
    # we will use validators imported from wtforms
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(),
                                             Email()])  # use Email validator to make sure an email address is entered
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    # use EqualTo
    # validator to make sure
    # password = confirm_password

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
                                             Email()])  # Using email since it's easy to forget usernames
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    # We have to set a secret key to our app protect it from modifying cookies, forgery attacks and cross site requests
    # To generate a secret key
    # Go to Terminal/Command line
    # Type - python
    # Type - import secrets
    # Type - secrets.token_hex(16) - 16 is the number of bytes
