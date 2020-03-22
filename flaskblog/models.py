from flaskblog import db
from datetime import datetime
from flaskblog import db


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
