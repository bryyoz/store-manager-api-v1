"""Product endpoints get and post methods"""
from flask_restplus import Namespace, Resource, reqparse, fields
from flask import make_response, jsonify

from ..models.Products import Product

ns_product = Namespace('Products')

product_models = ns_product.model("Store products",{
  "product_id":fields.Integer,
  "product_name":fields.String,
  "category":fields.String,
  "description":fields.String,
  "inventory":fields.String,
  "price":fields.String
  })

parser = reqparse.RequestParser()

parser.add_argument('product_name', required=True, help= 'This field cannot be blank')
parser.add_argument('category', required=True, help= 'This field cannot be blank')
parser.add_argument('description', required=True,help= 'This field cannot be blank')
parser.add_argument('inventory', required=True,help= 'This field cannot be blank')
parser.add_argument('price', required=True, help= 'This field cannot be blank')
    


@ns_product.route('')
class ProductEndpoint(Resource):
    """Contains all the endpoints for Product Model"""
    

    @ns_product.expect(product_models, validate = True)
    def post(self):
      args = parser.parse_args()

      product_name = args['product_name'] 
      if product_name == '' or product_name == None:
        return make_response(jsonify({'message':'cannot be empty'}))

      category = args['category']
      if category == '' or category == None:
        return make_response(jsonify({'message':'cannot be empty'}))

      description = args['description']
      if description == '' or description == None:
        return make_response(jsonify({'message':'cannot be empty'}))

      inventory  = args['inventory']
      if inventory == '' or inventory == None:
        return make_response(jsonify({'message':'cannot be empty'}))

      price = args['price']
      if price == '' or price == None:
        return make_response(jsonify({'message':'cannot be empty'}))

      
        
      result = Product(product_name, category, description, inventory, price)
      posted_product = result.post_product()
      
      return {'message':'Product created' }, 201

    
    def get(self):

        
        products = Product.get_all_products(self)
        return {'output':'These are the products in your inventory',
        'My products': products}, 200

@ns_product.route('/<int:product_id>')
class GetOneProduct(Resource):

    
    def get(self, product_id):

        
        one_product = Product.get_one_product(product_id)
        if one_product == 'product not available':
            return {'message': 'no product in inventory'}, 404
        return {'message': 'This is your product',
                'product': one_product}, 200

    