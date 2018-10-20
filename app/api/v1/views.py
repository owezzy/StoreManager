from flask import Flask
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource
from datetime import datetime
from models import ProductModel
from pytz import timezone


# timestamp set to local timezone
def local_timezone_time_stamp():
    tz = timezone('Africa/Nairobi')
    ct = datetime.now(tz=tz)
    return ct.isoformat()


class ProductManager():
    last_id = 0

    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.__class__.last_id += 1
        product.id = self.__class__.last_id
        self.products[self.__class__.last_id] = product

    def get_product(self, id):
        pass

    def delete_product(self, id):
        pass


product_fields = {
    'id': fields.Integer,
    'uri': fields.Url('product_endpoint'),
    'product_name': fields.String,
    'price': fields.Integer,
    'stock': fields.Integer,
    'creation_date': fields.DateTime

}

product_manager = ProductManager()


class Product(Resource):
    @staticmethod
    def abort_if_product_doesnt_exist(id):
        if id not in product_manager.products:
            abort(message="Message {0} doesn't exist".format(id), http_status_code=404)


class ProductList(Resource):
    @marshal_with(product_fields)
    def _post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('product_name', type=str, required=True, help='product_name cannot be empty!')
        parser.add_argument('price', type=int, required=True, help='price cannot be empty!')
        parser.add_argument('stock', type=int, required=True, help='Please specify the quantity!')
        args = parser.parse_args()
        product = ProductModel(
            product_name=args['product_name'],
            price=args['price'],
            stock=args['stock'],
            creation_date=local_timezone_time_stamp()
        )
        product_manager.add_product(product)
        return product, 201


app = Flask(__name__)
api = Api(app)
api.add_resource(ProductList, '/products/')
api.add_resource(Product, '/products/<int:id>', endpoint='product_endpoint')
