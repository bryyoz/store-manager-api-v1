'''
sets configuration for flask application
'''
from flask import Flask,Blueprint
from Instance.config import app_config
from app.api.V1 import app_V1

from flask_jwt_extended import (jwt_required, JWTManager, create_access_token, get_jwt_identity, get_raw_jwt)




def create_app(config_name):
	app = Flask(__name__,instance_relative_config= True)
	app.config.from_object(app_config[config_name])

	app.config['JWT_SECRET_KEY'] = 'super-power'
	jwt = JWTManager(app)
	
	app.register_blueprint(app_V1)
	return app
