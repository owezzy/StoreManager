import datetime
import re

from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_refresh_token_required, get_jwt_identity, jwt_required
from functools import wraps

from app.api.v2.models.users import User


def admin_only(admin):
    """Deny access to admin pages"""
    @wraps(admin)
    def decorator_function(*args, **kwargs):
        email = get_jwt_identity()
        user = User.find_by_email(email)
        if user['role'] != 1:
            return {'message': 'Only admin allowed Here'}, 401
        return admin(*args, **kwargs)

    return decorator_function


class UserRegistration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='This field cannot be blank')
    parser.add_argument('email', type=str, required=True, help='This field cannot be blank')
    parser.add_argument('password', type=str, required=True, help="This field cannot be blank")

    # create a new user
    @jwt_required
    @admin_only
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
        unique_name = User.find_by_email(email)
        if unique_name is not None:
            return {'message': 'Email already registered'}, 400

        password = User.generate_password_hash(raw_password)
        new_user = User(
            username=username,
            password=password,
            email=email
        )

        # save user instance to model
        result = User.create_new_user(new_user)
        return {
                   'message': 'User created successfully.',
                   'user': result
               }, 201


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
        current_user = User.find_by_email(email)
        if not current_user:
            return {'message': 'email {} does not exist'.format(email)}, 400
        db_password = current_user['password']
        pass_verify = User.check_hash(password, db_password)
        if not pass_verify:
            return {'message': 'Password doesnt match'}, 400
        access_token = create_access_token(identity=current_user['email'], expires_delta=datetime.timedelta(hours=3))
        return {
                   'message': 'User Login successful',
                   'status': 'ok',
                   'username': current_user['username'],
                   'access_token': access_token,
               }, 200


# token refresh object
class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}
