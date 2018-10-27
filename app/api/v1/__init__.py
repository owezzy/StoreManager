from flask_restful import Api
from flask import Flask, Blueprint

from app.api.v1.views import PostProduct, GetProduct, GetSingleProduct, PostOrder, GetOrder, GetSingleOrder

app = Flask(__name__)
version1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(version1)

api.add_resource(PostProduct, '/products/')
api.add_resource(GetProduct, '/products/')
api.add_resource(GetSingleProduct, '/products/<int:product_id>')
api.add_resource(PostOrder, '/sales/')
api.add_resource(GetOrder, '/sales/')
api.add_resource(GetSingleOrder, '/sales/<int:order_id>')
app.register_blueprint(version1)
