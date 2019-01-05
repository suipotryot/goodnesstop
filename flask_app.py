
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def top_list():
    return 'Hello from Flask!'


@app.route('/addtop/<topname>/')
def add_top(topname=None):
    return 'You added %s' % topname
