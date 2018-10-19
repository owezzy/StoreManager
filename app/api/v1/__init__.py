from flask_restful import Api
from flask import Blueprint

#from views import object

version1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(version1)

# api.add_resource(object, '/')