#importing endpoints of models


from flask import Blueprint
from flask_restplus import Api

from .views.sales import ns_sales
from .views.product import ns_product
from .views.registration import ns_register
from .views.login import ns_login

authorizations = {
	'apikey':{
	'type':'apiKey',
	'in':'header',
	'name':'x-api-key'
	}
}


app_V1 = Blueprint("V1",__name__)

api = Api(app_V1,title="Store Manager", version ="1",description="Store Manager v1", authorizations=authorizations)


api.add_namespace(ns_product, path='/api/V1/products')
api.add_namespace(ns_sales, path='/api/V1/sales')
api.add_namespace(ns_register, path='/api/V1/register')
api.add_namespace(ns_login, path='/api/V1/login')
	