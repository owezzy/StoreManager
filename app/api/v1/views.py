from flask_restful import abort, fields, marshal_with, reqparse, Resource
from datetime import datetime
from app.api.v1.models import ProductsModel, SalesModel
from pytz import timezone


# timestamp set to local timezone
def local_timezone_time_stamp():
    tz = timezone('Africa/Nairobi')
    ct = datetime.now(tz=tz)
    return ct


# product manager object
class ProductManager:
    last_id = 0

    # using a dictionary to hold product data
    def __init__(self):
        self.products = {}

    # adds a product to the list of products
    def add_product(self, product):
        self.__class__.last_id += 1
        product.id = self.__class__.last_id
        self.products[self.__class__.last_id] = product

    def get_product(self, id):
        return self.products[id]

    def delete_product(self, id):
        pass


# product fields data type definition
product_fields = {
    'id': fields.Integer,
    'product_name': fields.String,
    'price': fields.Integer,
    'stock': fields.Integer,
    'creation_date': fields.DateTime

}


# product custom validation
def input_validate(value, name):
    if isinstance(value, int):
        raise ValueError("The parameter '{}' cannot be a number".format(name, value))
    elif value == "":
        raise ValueError("product_name cannot be a empty")
    else:
        return value


product_manager = ProductManager()


# object to define products resource
class Product(Resource):
    # is executed in case of a request for product that doesn't exists.
    @staticmethod
    def abort_if_product_doesnt_exist(id):
        if id not in product_manager.products:
            abort(message="Product {0} doesn't exist".format(id), http_status_code=404)

    # fetch a single product
    @marshal_with(product_fields)
    def get(self, id):
        self.abort_if_product_doesnt_exist(id)
        return product_manager.get_product(id)


# object which holds the product list
class ProductList(Resource):
    # fetch all products from list
    @marshal_with(product_fields)
    def get(self):
        return [p for p in product_manager.products.values()]

    # add a product to the list
    @marshal_with(product_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('product_name', type=input_validate, required=True)
        parser.add_argument('price', type=int, required=True, help='can be a number only!')
        parser.add_argument('stock', type=int, required=True, help='Please specify a figure!')

        args = parser.parse_args()
        product = ProductsModel(
            product_name=args['product_name'],
            price=args['price'],
            stock=args['stock'],
            creation_date=local_timezone_time_stamp()
        )
        product_manager.add_product(product)
        return product, 201


"""sales resource"""


# sales manager object
class SalesManager:
    last_id = 0

    def __init__(self):
        self.orders = {}

    def add_order(self, order):
        self.__class__.last_id += 1
        order.id = self.__class__.last_id
        self.orders[self.__class__.last_id] = order

    def get_order(self, id):
        return self.orders[id]

    def delete_order(self, id):
        pass


# orders payload fields data types
order_fields = {
    'id': fields.Integer,
    'product_name': fields.String,
    'attendant_name': fields.String,
    'customer_name': fields.String,
    'quantity': fields.Integer,
    'cost': fields.Integer,
    'creation_date': fields.DateTime
}

sales_manager = SalesManager()


# Oder object to hold sales detail
class Order(Resource):
    @staticmethod
    def abort_if_order_doesnt_exist(id):
        if id not in sales_manager.orders:
            abort(
                message="Order {0} doesn't exist".format(id),
                http_status_code=404)

    # fetch a single order
    @marshal_with(order_fields)
    def get(self, id):
        self.abort_if_order_doesnt_exist(id)
        return sales_manager.get_order(id)


# OrderList object to store the sales order object
class OrderList(Resource):
    # get all sales orders
    @marshal_with(order_fields)
    def get(self):
        return [o for o in sales_manager.orders.values()]

    # add a single sales order to list
    @marshal_with(order_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('product_name', type=input_validate, required=True)
        parser.add_argument('customer_name', type=input_validate, required=True)
        parser.add_argument('attendant_name', type=input_validate, required=True)
        parser.add_argument(
            'cost', type=int, required=True, help='Cost value is not valid!')
        parser.add_argument(
            'quantity', type=int, required=True, help='Please specify the quantity!')

        args = parser.parse_args()
        order = SalesModel(
            product_name=args['product_name'],
            customer_name=args['customer_name'],
            attendant_name=args['attendant_name'],
            cost=args['cost'],
            quantity=args['quantity'],
            creation_date=local_timezone_time_stamp())
        sales_manager.add_order(order)
        return order, 201
