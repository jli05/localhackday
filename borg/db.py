
import sqlite3

def get_posts(db, page_id=0, posts_per_page=None):
    ''' Get list of posts '''
    assert page_id >= 0
    assert posts_per_page > 0

    with sqlite3.connect(db) as conn:
        (c,) = conn.execute('SELECT COUNT(*) FROM posts').fetchone()

        cur = conn.execute('SELECT * FROM posts WHERE rowid'
                           ' BETWEEN ? AND ?', (c - (page_id + 1)
                                                    * posts_per_page + 1,
                                                c - page_id * posts_per_page))
        posts = cur.fetchall()

        return posts
