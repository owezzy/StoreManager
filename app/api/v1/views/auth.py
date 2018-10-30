import re

from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity

from app.api.v1.models.users import User


class UserRegistration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='This field cannot be blank')
    parser.add_argument('email', type=str, required=True, help='This field cannot be blank')
    parser.add_argument('password', type=str, required=True, help="This field cannot be blank")

    # create a new user
    def post(self):
        args = UserRegistration.parser.parse_args()
        # cleanup data
        username = args.get('username').strip()
        email = args.get('email')
        raw_password = args.get('password')

        # validate user data input
        email_validation = re.compile(r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[.a-zA-Z-]+$)")
        username_validation = re.compile(r"(^[A-Za-z0-9-]+$)")

        if not email:
            return make_response(jsonify({'message': 'Email is required'}), 400)
        if not raw_password:
            return make_response(jsonify({'message': 'Password is a required field'}), 400)
        if not username:
            return make_response(jsonify({'message': 'Username is a required field'}), 400)
        if len(raw_password) < 4:
            return make_response(jsonify({'message': 'Password should have a a minimum of 4 characters'}), 400)
        if not (re.match(email_validation, email)):
            return make_response(jsonify({'message': ' Please provide a valid email address'}), 400)
        if not (re.match(username_validation, username)):
            return make_response(jsonify({'message': 'Username can have Alphabets and Numeric, no special characters'}),
                                 400)

        # on successful validation
        current_user = User.find_by_email_address(email)
        if current_user != False:
            return {'message': 'Email already registered'}, 400

        current_user = User.find_by_username(username)
        if current_user != False:
            return {'message': 'username already exist'}, 400

        # validate current user
        this_user = User.find_by_email_address(email)
        if this_user != False:
            return {'message': 'Email already registered'}, 400

        password = User.generate_password_hash(raw_password)
        current_user = User(
            username=username,
            password=password,
            email=email
        )

        # save user instance to model
        try:
            result = User.create_new_user(current_user)
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)

            return {
                       'message': 'User created successfully.',
                       'access_token': access_token,
                       'refresh_token': refresh_token,
                       'user': result
                   }, 201

        except Exception as error:
            print(error)
            return {'message': 'Something went wrong'}, 500


# user login functionality
class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', required=True, help='This field cannot be blank')
    parser.add_argument('password', required=True, help="This field cannot be blank")

    # login function
    def post(self):
        # clean data first
        args = UserLogin.parser.parse_args()
        password = args.get('password').strip()
        email = args.get('email').strip()
        if not email:
            return {'message': 'Email field can not be empty'}, 400
        if not password:
            return {'message': 'Password field cannot be empty'}, 400
        # upon successful validation of user by the email
        current_user = User.find_by_email_address(email)
        if current_user == False:
            return {'message': 'email {} does not exist'.format(email)}, 400
        db_password = current_user['password']
        return User.check_hash(password, db_password)
        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)
        return {
                   'message': 'User Login successful',
                   'status': 'ok',
                   'access_token': access_token,
                   'refresh_token': refresh_token
               }, 200


# token refresh object
class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}
