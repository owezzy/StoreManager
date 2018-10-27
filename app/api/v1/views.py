from flask_restful import reqparse, Resource, abort
from app.api.v1.models import ProductsModel, SalesModel


# object to define product resource
class GetProduct(Resource):

    @staticmethod
    def get():
        all_products = ProductsModel.get_all_product()
        return {
                   'message': 'All Products retrieved successfully',
                   'status': 'ok',
                   # 'access_token': access_token,
                   # 'refresh_token': refresh_token,
                   'product': all_products
               }, 200


class GetSingleProduct(Resource):
    # retrieve a single product
    @staticmethod
    def get(product_id):
        single_product = ProductsModel.get_product(product_id)
        return {
                   'message': 'Product retrieved successfully',
                   'status': 'ok',
                   # 'access_token': access_token,
                   # 'refresh_token': refresh_token,
                   'product_detail': single_product
               }, 200


# object which holds the product list
class PostProduct(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('product_name', type=str, required=True)
        parser.add_argument('price', type=int, required=True, help='can be a number only!')
        parser.add_argument('stock', type=int, required=True, help='Please specify a figure!')

        args = parser.parse_args()
        product_name = args.get('product_name')
        price = args.get('price')
        stock = args.get('stock')

        # check if product_name exits

        check_product_name = ProductsModel.check_product_name(product_name)
        if check_product_name != False:
            return {'message': 'Product Name already Exits'}

        # parse instance data to model
        product = ProductsModel(
            product_name=product_name,
            price=price,
            stock=stock,
        )

        try:
            result = product.add_product()
            return {
                       'message': 'Product was created successfully',
                       'status': 'CREATED',
                       # 'access_token': access_token,
                       # 'refresh_token': refresh_token,
                       'product_detail': result
                   }, 201
        except Exception as er:
            print(er)
        return {'message': 'Something went wrong'}, 500


# Oder object to hold sales detail
class GetOrder(Resource):
    @staticmethod
    def get():
        all_orders = SalesModel.get_all_orders()
        return {
                   'message': 'All Orders retrieved successfully',
                   'status': 'ok',
                   # 'access_token': access_token,
                   # 'refresh_token': refresh_token,
                   'product': all_orders
               }, 200


class GetSingleOrder(Resource):
    # fetch a single order
    @staticmethod
    def get(order_id):
        single_order = SalesModel.get_order(order_id)
        return {
                   'message': 'Order retrieved successfully',
                   'status': 'ok',
                   # 'access_token': access_token,
                   # 'refresh_token': refresh_token,
                   'product': single_order
               }, 200


# OrderList object to store the sales order object
class PostOrder(Resource):
    # add a single sales order to list
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('product_name', type=str, required=True)
        parser.add_argument('customer_name', type=str, required=True)
        parser.add_argument('attendant_name', type=str, required=True)
        parser.add_argument(
            'cost', type=int, required=True, help='Cost value is not valid!')
        parser.add_argument(
            'quantity', type=int, required=True, help='Please specify the quantity!')

        args = parser.parse_args()
        product_name = args.get('product_name')
        customer_name = args.get('customer_name')
        attendant_name = args.get('attendant_name')
        cost = args.get('cost')
        quantity = args.get('quantity')

        new_order = SalesModel(
            product_name=product_name,
            customer_name=customer_name,
            cost=cost,
            quantity=quantity,
            attendant_name=attendant_name
        )
        try:
            result = new_order.add_order()
            return {
                       'message': 'Order was created successfully',
                       'status': 'CREATED',
                       # 'access_token': access_token,
                       # 'refresh_token': refresh_token,
                       'order': result
                   }, 201
        except Exception as er:
            print(er)
            return {'message': 'Something went wrong'}, 500
