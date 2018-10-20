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
  "inventory":fields.Integer,
  "price":fields.Integer
  })


@ns_product.route('')
class ProductEndpoint(Resource):
    """Contains all the endpoints for Product Model"""

    @ns_product.expect(product_models)
    def post(self):
      parser = reqparse.RequestParser()

      parser.add_argument('product_name', required=True, type=str, help='Please input product name', location=['json'])
      parser.add_argument('category', required=True, type=str, help='Please input product category', location=['json'])
      parser.add_argument('description', required=True, type=str, help='Please input commodity description', location=['json'])
      parser.add_argument('price', required=True, type=int, help='Please input price of commodity', location=['json'])
    



      args = parser.parse_args()
      product_name = args['product_name']
      category = args['category']
      description = args['description']
      price = args['price']
        
      result = Product(product_name, category, description, category, price)
      posted_product = result.post_product()
      
      return {'output': 'Product created' }, 201

    
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

    