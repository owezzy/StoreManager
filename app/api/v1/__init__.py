from flask_restful import Api
from flask import Flask, Blueprint

from app.api.v1.views.products import PostProduct, GetProduct, GetSingleProduct
from app.api.v1.views.sales import PostOrder, GetOrder, GetSingleOrder
from app.api.v1.models.products import ProductsModel
from app.api.v1.views.auth import UserRegistration, UserLogin, TokenRefresh

app = Flask(__name__)
version1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(version1)

api.add_resource(PostProduct, '/products/')
api.add_resource(GetProduct, '/products/')
api.add_resource(GetSingleProduct, '/products/<int:product_id>')
api.add_resource(PostOrder, '/sales/')
api.add_resource(GetOrder, '/sales/')
api.add_resource(GetSingleOrder, '/sales/<int:order_id>')
api.add_resource(UserRegistration, '/registration/')
api.add_resource(UserLogin, '/login/')
api.add_resource(TokenRefresh, '/token/refresh')
app.register_blueprint(version1)
