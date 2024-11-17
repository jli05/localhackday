
from flask import current_app, request, Blueprint, render_template, redirect
from .db import authorise, add_post
from datetime import datetime

bp = Blueprint('publish', __name__)

@bp.route('/publish', methods=('GET', 'POST'))
def publish_post():
    ''' Publish a post '''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        res = authorise(current_app.config['PUBLISHERS_DB'],
                        username, password)
        if not res:
            return 'Unauthorised access', 401

        (publisher, email, notes) = res
        title = request.form['title']
        body = request.form['body']
        add_post(current_app.config['POSTS_DB'],
                 title, body, publisher, email,
                 datetime.now().strftime('%Y-%m-%dT%H:%M:%S'))
        return redirect('/')

    else:
        return render_template('publish.html')
