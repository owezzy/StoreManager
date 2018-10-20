from flask_restful import Api
from flask import Blueprint

from views import ProductList, Product

version1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(version1)
api.add_resource(ProductList, '/products/')
api.add_resource(Product, '/products/<int:id>', endpoint='product_endpoint')