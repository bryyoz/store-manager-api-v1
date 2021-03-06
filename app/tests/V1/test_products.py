import unittest


import sys # fix import errors
import os
#sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import create_app
import json


class TestProducts(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context =self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        self.product_record = {
                            "product_id":1,
                            "product_name":"television",
                            "category":"electricals",
                            "product_description":"oled",
                            "inventory":50,
                            "price":23450 
                          }


        


    def user_authentication_register(self, email="kip@gmail.com", password="1234", re_password="1234"):
        """Method to register a User"""
        user_register = {
            'email': email,
            'password': password,
            're_password': re_password
        }
        return self.client.post('/api/V1/register', data=user_register)

    def user_authentication_login(self, email="kip@gmail.com", password="1234"):
        """Method to login a User"""
        user_login = {
            'email': email,
            'password': password
        }
        return self.client.post('/api/V1/login', data=user_login)



    
   

    def test_get_all_products(self):
        """These tests check all products record """

        response=self.client.get('/api/V1/products')

        res=json.loads(response.data.decode())
        self.assertEqual(res['output'],'These are the products in your inventory')
        self.assertEqual(response.status_code,200)

    def test_get_one_product(self):
        """These tests check  specific products record """
 
        response = self.client.get('/api/V1/products/1', content_type="application/json")
        self.assertTrue(response.status_code, 200)



    def test_nonexistant_products_id(self):
        """Test check none existing products_id """
        response = self.client.get('/api/V1/products/20', content_type="application/json")
        self.assertEqual(response.status_code,404)

    
    def test_post_products(self):
        """These tests check for all posts posted"""

        self.user_authentication_register()

        response = self.user_authentication_login()

        token_admin = json.loads(response.data.decode()).get("x-api-key")

        result = self.client.post('/api/V1/products', headers=dict(Authorization ="Bearer {}".format(token_admin)),
                        data=self.product_record)
                                            
        res=json.loads(result.data.decode())

        #self.assertEqual(res['output'],'Product created')
        self.assertEqual(result.status_code, 401)





def teardown(self):
    self.product_record = {}
