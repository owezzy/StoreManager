from flask import Flask
from instance.config import app_config


def create_app(config):
    """ creates a flask instance according to config passed """
    app = Flask(__name__)
    app.config.from_object(app_config[config])
    # versions of api
    from app.api.v1 import version1 as v1
    app.register_blueprint(v1)
    return app
