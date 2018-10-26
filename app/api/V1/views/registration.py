import re
from flask import Flask, jsonify, make_response, request
from flask_restplus import Api, Resource, Namespace, reqparse, fields
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from ..models.Users import User

ns_register = Namespace('Authentication')


user_model = ns_register.model('Registration',{
		'email': fields.String(required=True, description='user email address'),
		'role':fields.String,
        'password': fields.String(required=True, description='user password'),
        're_password': fields.String(required=True, description='user password')
	})


parser = reqparse.RequestParser()
parser.add_argument('email')
parser.add_argument('role')
parser.add_argument('password')
parser.add_argument('re_password')

valid_email = r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)"


@ns_register.route('')
class UserRegistration(Resource):
	"""All products class"""

	@ns_register.expect(user_model)
	def post(self):
		"""Register a new user"""
		
		args = parser.parse_args()
		email = args['email']
		role =args['role']
		password = args['password']
		re_password = args['re_password']
		

		new_user = User.get_one_user(self, email)

		if not re.match(valid_email, email):
			return jsonify({"message": "Please enter a valid email address"})

		if password == '' or password == ' ':
			return make_response(jsonify({'message': 'please enter your password',
                                          'status': 'login failed'}), 401)

		if password != re_password:
			return make_response(jsonify({'message': 'passwords do not match',
                                          'status': 'failed'}), 401)


		user = [user for user in User.all_users if user['email'] == email]
		if not user:
			new_user = User(email, role, password, re_password)
			new_user.signup()
			
			return make_response(jsonify({"message":"User created!"}), 201)
		else:
			return make_response(jsonify({'message':'Email already exists.'}), 201)


