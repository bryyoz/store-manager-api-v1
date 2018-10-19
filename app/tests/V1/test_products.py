import unittest


import sys # fix import errors
import os
#sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import create_app
import json


products_data = [{
    "product_id":1,
    "product_name":"television",
    "category":"electricals",
    "product_description":"oled",
    "inventory":50,
    "price":23450
    
}]


class TestClient(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context =self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    
    def test_post_products(self):
        """These tests check for all posts posted"""
        response = self.client.post('/api/V1/products',data=json.dumps(products_data[0]),
            content_type='application/json')

        res=json.loads(response.data.decode())

        self.assertEqual(res['output'],'Product record has been created')
        self.assertEqual(response.status_code, 201) 
        


    def test_get_all_products(self):
        """These tests check all products record """
        response=self.client.get('/api/V1/products')

        res=json.loads(response.data.decode())
        self.assertEqual(res['output'],'These are your products records')
        self.assertEqual(response.status_code,200)

    def test_get_one_sale(self):
        """These tests check  specific products record """ 
        response = self.client.get('/api/V1/products/1', content_type="application/json")
        self.assertTrue(response.status_code, 200)



    def test_wrong_id(self):
        """These tests when wrong id is entered"""
        products_id = "a" 
        response = self.client.get('/api/V1/products/' + products_id)
        self.assertRaises(TypeError,response) 


    def test_nonexistant_products_id(self):
        """Test check none existing products_id """
        response = self.client.get('/api/V1/products/20', content_type="application/json")
        self.assertEqual(response.status_code,404)



    






def teardown(self):
    self.app_context.pop()
