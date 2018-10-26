import re
import datetime
import jwt

from Instance.config import Config
from functools import wraps
from flask import Flask, jsonify, make_response, request
from flask_restplus import Api, Resource, Namespace, reqparse, fields
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from ..models import *
from ..models.Users import User


ns_login = Namespace('Authentication')


login_model = ns_login.model('Login',{
		'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password')

	})

parser = reqparse.RequestParser()
parser.add_argument('email', required=True, help="email cannot be blank")
parser.add_argument('password', required=True, help="password cannot be blank")

valid_email = r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)"


def jwt_required(f):
    @wraps(f)
    def decorated(*arg,**kwargs):
        token = None
        current_user = None
        if 'x-api-key' in request.headers:
            token = request.headers['x-api-key']
        if not token:
            return {'result': 'token is missing'},401
        try:
            data = jwt.decode(token, Config.SECRET_KEY)
            for user in User.all_users:
                if user['email'] == data['email']:
                    current_user = user

        except:
        	return {'result': 'token is invalid'},401
        return f(current_user, *arg, **kwargs)
    return decorated


@ns_login.route('')
class UserLogin(Resource):
	'''user login class'''
	
	@ns_login.expect(login_model)
	def post(self):

		args = parser.parse_args()
		email = args['email']
		password = args['password']


		user = [user for user in User.all_users if user['email'] == email]

		if not user: 
			return make_response(jsonify({"message":"Your account does not exist!, Please Register!"}), 401)

		if not re.match(valid_email, email):
			return jsonify({"message": "Please enter a valid email address"})

		if User.password == '' or password == None:
			return make_response(jsonify({'message': 'please enter your password',
                                              'status': 'failed'}), 401)
		for user in User.all_users:
			if email == user["email"] and password == user["password"]:
				token = jwt.encode({
                    "email": email,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta
                                  (minutes=60)
                }, Config.SECRET_KEY)
				return make_response(jsonify({
						     "token": token.decode("UTF-8")}), 200)
			return make_response(jsonify({
            "Message": "Login failed"
        }
        ), 401)
	




		
        