"""Sales_Records get and post methods"""
from flask_restplus import Namespace, Resource, reqparse, fields
from flask import make_response, jsonify

from ..models.Sales import Sales

ns_sales = Namespace('Sales')

sales_models = ns_sales.model("Store sales",{
	"sale_id":fields.Integer,
	"names":fields.String,
	"cart":fields.Integer,
	"total_price":fields.Integer
	})


@ns_sales.route('')
class SalesRecords(Resource):

	
	@ns_sales.expect(sales_models)
	def post(self):
		parser = reqparse.RequestParser()

		parser.add_argument('names', required=True, type=str, help='Please input your name', location=['json'])
		parser.add_argument('cart')
		parser.add_argument('total_price', required=True, type=int, help='Please input a total price', location=['json'])

		args = parser.parse_args()
		names = args['names']
		cart = args['cart']
		total_price  = args['total_price']
		
		result = Sales(names,cart, total_price)
		posted_sale = result.post_sales()



		return {'output': 'Sale record has been created'}, 201



	def get(self):
		response = Sales.get_all_sales(self)
		return {'output':'These are your sales records',
		"Sales Records":response}, 200




@ns_sales.route('/<int:sale_id>')
class OneSaleRecord(Resource):


	def get(self, sale_id):
		response = Sales.get_one_sale(sale_id)
		if response == 'sale record not available':
			return {'message': 'There is no sale record found'}, 404
		return make_response(jsonify({'message': 'This is your sale record',
                                      'product': response}), 200)


	
		




 