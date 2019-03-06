from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/home')
def home():
    return 'Home'

@app.route('/about')
def about():
    return 'About'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'post: %s' %post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'subpath %s' %subpath

@app.route('/project/')
def project():
    return 'project'

#************************************