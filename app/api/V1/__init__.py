#importing endpoints of models


from flask import Blueprint
from flask_restplus import Api

from .views.sales import ns_sales





app_V1 = Blueprint("V1",__name__)

api = Api(app_V1,title="Store Manager", version ="1",description="Store Manager v1")


#api.add_namespace(ns_product, path='/api/V1/products')
api.add_namespace(ns_sales, path='/api/V1/sales')
#api.add_namespace(ns_auth, path='/api/V1/register')
#api.add_namespace(ns_auth, path='/api/V1/login')
	