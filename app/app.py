from flask import Flask
from config import app_config
from flask_jwt_extended import JWTManager


def create_app(config):
    """ creates a flask instance according to config passed """
    app = Flask(__name__)
    app.config.from_object(app_config[config])
    # versions of api
    from app.api.v1 import version1 as v1
    app.register_blueprint(v1)

    # registerd JWT manager
    app.config['JWT_SECRET_KEY'] = 'owezzy'
    jwt = JWTManager(app)
    return app
