
from flask import current_app, request, Blueprint, render_template
from .db import get_posts

bp = Blueprint('homepage', __name__)

@bp.route('/')
def list_posts():
    ''' Landing page '''
    page_id = request.args.get('p')
    if page_id:
        page_id = int(page_id)
    else:
        page_id = 0

    posts = get_posts(current_app.config['POSTS_DB'], page_id=page_id,
                      posts_per_page=current_app.config['POSTS_PER_PAGE'])

    return render_template('index.html', posts=posts)
