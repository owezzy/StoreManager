from flask_restful import Api
from flask import Flask, Blueprint

from app.api.v1.views import ProductList, Product


app = Flask(__name__)
version1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(version1)

api.add_resource(ProductList, '/products')
api.add_resource(Product, '/products/<int:id>')
app.register_blueprint(version1)
