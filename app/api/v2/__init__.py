from flask_restful import Api
from flask import Flask, Blueprint

from app.api.v2.views.products import PostProduct, GetProduct, GetSingleProduct
from app.api.v2.views.sales import PostOrder, GetOrder, GetSingleOrder
from app.api.v2.models.products import ProductsModel
from app.api.v2.views.auth import UserRegistration, UserLogin, TokenRefresh

app = Flask(__name__)
version2 = Blueprint('api', __name__, url_prefix='/api/v2')
apiv2 = Api(version2)

apiv2.add_resource(PostProduct, '/products/')
apiv2.add_resource(GetProduct, '/products/')
apiv2.add_resource(GetSingleProduct, '/products/<int:product_id>')
apiv2.add_resource(PostOrder, '/sales/')
apiv2.add_resource(GetOrder, '/sales/')
apiv2.add_resource(GetSingleOrder, '/sales/<int:order_id>')
apiv2.add_resource(UserRegistration, '/registration/')
apiv2.add_resource(UserLogin, '/login/')
apiv2.add_resource(TokenRefresh, '/token/refresh')
app.register_blueprint(version2)
