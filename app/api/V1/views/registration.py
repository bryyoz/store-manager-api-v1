from flask import Flask, jsonify, make_response, request
from flask_restplus import Api, Resource, Namespace, reqparse, fields
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from ..models.Users import User

ns_register = Namespace('Authentication')


user_model = ns_register.model('Registration',{
		'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
      

	})


parser = reqparse.RequestParser()
parser.add_argument('email', required=True, help="email cannot be blank")
parser.add_argument('username')
parser.add_argument('password', required=True, help="password cannot be blank")

@ns_register.route('')
class UserRegistration(Resource):
	"""All products class"""

	@ns_register.expect(user_model)
	def post(self):
		"""Register a new user"""
		
		args = parser.parse_args()
		email = args['email']
		username = args['username']
		password = args['password']
		
		new_user = User.get_one_user(self, email)

		if new_user == "User not found":
			new_user = User(email, username, password)
			new_user.signup()

			return make_response(jsonify(
				{"message":"User created!",
				"user":new_user.__dict__}
				), 201)
		else:
			return make_response(jsonify({'message':'Email already exists.'}))


