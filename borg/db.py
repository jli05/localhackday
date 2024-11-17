
import sqlite3
from werkzeug.security import check_password_hash

def get_posts(db, page_id=0, posts_per_page=None):
    ''' Get list of posts '''
    assert page_id >= 0
    assert posts_per_page > 0

    with sqlite3.connect(db) as conn:
        cur = conn.execute('SELECT * FROM posts'
                           ' ORDER BY time DESC'
                           ' LIMIT ? OFFSET ?',
                           ((page_id + 1) * posts_per_page,
                            page_id * posts_per_page))
        posts = cur.fetchall()

        return posts

def add_post(db, title=None, body=None,
             publisher=None, email=None, time=None):
    ''' Add one post '''
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO posts VALUES (?, ?, ?, ?, ?)',
                     (title, body, publisher, email, time))

def authorise(users_db, username, password):
    ''' Check the credentials of an user '''
    with sqlite3.connect(users_db) as conn:
        res = conn.execute('SELECT * FROM users WHERE email == ?',
                           (username,)).fetchone()
        if res:
            (username, email, notes, password_hash) = res
            if check_password_hash(password_hash, password):
                return (username, email, notes)

    return None
