from flask import Flask
from instance.config import app_config
from werkzeug.contrib.fixers import ProxyFix


def create_app(config_name='development'):
    """ creates a flask instance according to config passed """
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')
    app.wsgi_app = ProxyFix(app.wsgi_app)

    # versions of api
    from app.api.v1 import version1 as v1
    app.register_blueprint(v1)
    return app


APP = create_app()
