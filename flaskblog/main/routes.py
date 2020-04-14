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
    return render_template('cov.html', title='COVID-19')


@main.route('/about')
def about():
    return render_template('about.html', title='About')
