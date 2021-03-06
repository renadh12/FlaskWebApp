from flask import render_template, request, Blueprint
from flaskblog.models import Post

# We have to set a secret key to our main protect it from modifying cookies, forgery attacks and cross site requests
# To generate a secret key
# Go to Terminal/Command line
# Type - python
# Type - import secrets
# Type - secrets.token_hex(16) - 16 is the number of bytes
# Copy the secret key and set it equal to app.config['SECRET_KEY']

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)  # default page set to 1
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route('/cov')
def cov():
    page = request.args.get('page', 1, type=int)  # default page set to 1
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('cov.html', title='COVID-19', posts=posts)


@main.route('/tech')
def tech():
    page = request.args.get('page', 1, type=int)  # default page set to 1
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('tech.html', title='Tech', posts=posts)

@main.route('/fut')
def fut():
    page = request.args.get('page', 1, type=int)  # default page set to 1
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('fut.html', title='FUT', posts=posts)

@main.route('/about')
def about():
    return render_template('about.html', title='About')

@main.route('/human')
def human():
    return render_template('human.html', title='The Side Project')

@main.route('/humantwo')
def human_two():
    return render_template('humantwo.html', title='The Side Project')

@main.route('/comingsoon')
def coming_soon():
    return render_template('comingsoon.html', title='The Side Project')

@main.route('/nera')
def nera():
    return render_template('side.html', title='The Side Project : Asmaa Amadou')

@main.route('/asmaa')
def asmaa():
    return render_template('asmaa.html', title='The Side Project')
