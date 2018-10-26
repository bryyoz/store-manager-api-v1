"""Sales_Records get and post methods"""
import jwt
from flask_restplus import Namespace, Resource, reqparse, fields
#from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_claims)
from flask import make_response, jsonify

from ..models.Sales import Sales
from ..views.login import jwt_required
# from ..models.Users import jwt_required

ns_sales = Namespace('Sales')

sales_models = ns_sales.model("Store sales",{
	"sale_id":fields.Integer,
	"names":fields.String,
	"cart":fields.Integer,
	"total_price":fields.Integer
	})


@ns_sales.route('')
class SalesRecords(Resource):

	@jwt_required
	@ns_sales.expect(sales_models)
	@ns_sales.doc(security = 'apikey')
	def post(self, current_user):
		if current_user["role"] != "attendant":
			return make_response(jsonify({
                "Message": "only attendant can post sales"} ), 403)


		
		parser = reqparse.RequestParser()

		parser.add_argument('names')
		parser.add_argument('cart')
		parser.add_argument('total_price')

		args = parser.parse_args()
		names = args['names']

		if names == '' or names == None:
			return make_response(jsonify({'message':'cannot be empty'}))
		
		cart = args['cart']
		if cart == '' or cart == None:
			return make_response(jsonify({'message':'cannot be empty'}))


		total_price  = args['total_price']
		if total_price == '' or total_price == None:
			return make_response(jsonify({'message':'cannot be empty'}))
		
		result = Sales(names,cart, total_price)
		posted_sale = result.post_sales()



		return {'output': 'Sale record has been created'}, 201



	def get(self):
		response = Sales.get_all_sales(self)
		return {'output':'These are your sales records',
		"Sales Records":response}, 200




@ns_sales.route('/<int:sale_id>')
class OneSaleRecord(Resource):

	@jwt_required
	@ns_sales.doc(security = 'apikey')
	def get(self, current_user, sale_id):
		if current_user["role"] != "admin":
			return make_response(jsonify({
                "Message": "Access denied"}
            ), 403)


		response = Sales.get_one_sale(sale_id)
		if response == 'sale record not available':
			return {'message': 'There is no sale record found'}, 404
		return make_response(jsonify({'message': 'This is your sale record',
                                      'product': response}), 200)


	
		




 