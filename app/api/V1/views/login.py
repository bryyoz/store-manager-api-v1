from flask import Flask, jsonify, make_response, request
from flask_restplus import Api, Resource, Namespace, reqparse, fields
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from ..models.Users import User

ns_login = Namespace('Authentication')


login_model = ns_login.model('Login',{
		'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
      

	})


parser = reqparse.RequestParser()
parser.add_argument('email', required=True, help="email cannot be blank")
parser.add_argument('password', required=True, help="password cannot be blank")



@ns_login.route('')
class UserLogin(Resource):
	'''user login class'''
	
	@ns_login.expect(login_model)
	def post(self):

		args = parser.parse_args()
		email = args['email']
		password = args['password']


		# get user by email to check if user exists
		
		user = User.get_one_user(self, email)

		if email and user == "User not found":
			return make_response(jsonify(
				{
				"message":"Your account does not exist!, Please Register!",
				}), 401)
		if User.password == '' or password == None:
			return make_response(jsonify({'message': 'please enter your password',
                                              'status': 'failed'}), 401)
		else:
			if user and User.validate_user_password(password):
				token =create_access_token(['email'])
				return make_response(jsonify({'message': 'Logged in successfully!', 'token': token}), 201)

			
	
        

        