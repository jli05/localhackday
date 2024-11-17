from flask import Flask

def create_app():
    ''' Create app '''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py', silent=True)

    from . import homepage, publish
    app.register_blueprint(homepage.bp)
    app.register_blueprint(publish.bp)

    return app

app = create_app()

@app.after_request
def add_security_headers(res):
    res.headers['Content-Security-Policy'] = "connect-src 'self'"
    res.headers['X-Content-Type-Options'] = 'nosniff'
    res.headers['X-Frame-Options'] = 'SAMEORIGIN'
    res.headers['X-XSS-Protection'] = '1; mode=block'
    if app.config['PROD']:
        res.headers['Strict-Transport-Security'] = ('max-age=31536000; '
                                                    'includeSubDomains')
    return res
