'''
sets configuration for flask application
'''
from flask import Flask,Blueprint
from Instance.config import app_config
from app.api.V1 import app_V1



def create_app(config_name):
	app = Flask(__name__,instance_relative_config= True)
	app.config.from_object(app_config[config_name])


	
	
	app.register_blueprint(app_V1)
	return app
