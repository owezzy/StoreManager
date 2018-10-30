from flask import make_response, jsonify
from flask_restful import reqparse, Resource
from flask_jwt_extended import jwt_required
from app.api.v1.models.sales import SalesModel


# Oder object to hold sales detail
class GetOrder(Resource):
    @jwt_required
    def get(self):
        all_orders = SalesModel.get_all_orders()
        return {
                   'message': 'All Orders retrieved successfully',
                   'status': 'ok',
                   'product': all_orders
               }, 200


class GetSingleOrder(Resource):
    # fetch a single order
    @jwt_required
    def get(self, order_id):
        single_order = SalesModel.get_order(order_id)
        return {
                   'message': 'Order retrieved successfully',
                   'status': 'ok',
                   'product': single_order
               }, 200


# OrderList object to store the sales order object
class PostOrder(Resource):
    # add a single sales order to list
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('product_name', type=str, required=True)
        parser.add_argument('customer_name', type=str, required=True)
        parser.add_argument('attendant_name', type=str, required=True)
        parser.add_argument(
            'cost', type=int, required=True, help='Cost value is not valid!')
        parser.add_argument(
            'quantity', type=int, required=True, help='Please specify the quantity!')

        args = parser.parse_args()
        product_name = args.get('product_name').strip()
        customer_name = args.get('customer_name').strip()
        attendant_name = args.get('attendant_name').strip()
        cost = args.get('cost')
        quantity = args.get('quantity')
        # validation error
        if not product_name:
            return make_response(jsonify({'message': 'product_name can not be empty'}), 400)
        if not customer_name:
            return make_response(jsonify({'message': 'please specify customer name!'}), 400)
        if not attendant_name:
            return make_response(jsonify({'message': 'please specify attendant name!'}), 400)
        if not cost:
            return make_response(jsonify({'message': 'please specify cost of product!'}), 400)
        if not quantity:
            return make_response(jsonify({'message': 'please specify quantity!'}), 400)

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
                       'order': result
                   }, 201
        except Exception as er:
            print(er)
            return {'message': 'Something went wrong'}, 500
