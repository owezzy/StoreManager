from flask import Flask
from config import app_config
from flask_jwt_extended import JWTManager
from .db import create_tables


def create_app(config_name):
    """ creates a flask instance according to config passed """
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    # versions of api
    from app.api.v2 import version2 as v2

    app.register_blueprint(v2)

    # registered JWT manager
    app.config['JWT_SECRET_KEY'] = 'owezzy'
    jwt = JWTManager(app)

    create_tables()

    return app
