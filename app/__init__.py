from flask import Flask


def create_app(config_filename):
    """ creates a flask instance according to config passed """
    app = Flask(__name__)
    app.config.from_object(config_filename)
    # app.url_map.strict_slashes = False

    # versions of api
    from app.api.v1 import version1 as v1
    app.register_blueprint(v1)
    return app
