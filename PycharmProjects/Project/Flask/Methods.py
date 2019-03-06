from flask import Flask,request,render_template,url_for
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method('POST'):
        return do_the_login()
    else:
        return show_the_login_from()

#Static files
@app.route('/')
def index():
    return 'The static url is:{0}'.format(url_for('static',filename='style.css'))

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('main.html',name=name)