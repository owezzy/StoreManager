from flask import make_response, jsonify
from flask_restful import reqparse, Resource
from flask_jwt_extended import jwt_required
from app.api.v1.models import ProductsModel


# object to define product resource
class GetProduct(Resource):
    @jwt_required
    def get(self):
        all_products = ProductsModel.get_all_product()
        return {
                   'message': 'All Products retrieved successfully',
                   'status': 'ok',
                   'product': all_products
               }, 200


class GetSingleProduct(Resource):
    # retrieve a single product
    @jwt_required
    def get(self, product_id):
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

    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('product_name', type=str, required=True)
        parser.add_argument('price', type=int, required=True, help='can be a number only!')
        parser.add_argument('stock', type=int, required=True, help='Please specify a figure!')

        # strip white space
        args = parser.parse_args()
        product_name = args.get('product_name').strip()
        price = args.get('price')
        stock = args.get('stock')

        # validation error
        if not product_name:
            return make_response(jsonify({'message': 'product_name can not be empty'}), 400)
        if not price:
            return make_response(jsonify({'message': 'please specify product Price!'}), 400)
        if not stock:
            return make_response(jsonify({'message': 'please specify product Price!'}), 400)

        # check if product_name exits
        check_product_name = ProductsModel.check_product_name(product_name)
        if check_product_name != False:
            return make_response(jsonify({'message': 'Product Name already Exits'}), 400)

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
