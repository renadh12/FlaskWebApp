from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "c792f0e1522c28a04c94ac14e51e6647"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"  # three forward slashes for relative path to the current
# directory
db = SQLAlchemy(app)  # Set up db instance

from flaskblog import routes
