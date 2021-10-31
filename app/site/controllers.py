from flask import render_template

from app.site import site

@site.route('/')
def index():
    return render_template('site/index.html')

@site.route('/post', methods=['POST', 'GET'])
def post():
    return render_template('site/post.html')