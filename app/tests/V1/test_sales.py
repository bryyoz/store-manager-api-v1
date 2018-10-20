import unittest


import sys # fix import errors
import os
#sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.apps import create_app
import json


products_data = [{
    "sales_id":1,
    "names":"josh kie",
    "items_sold":50,
    "total_sales":2345,
    
}]


class TestClient(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context =self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    
    def test_post_sales(self):
        """These tests check for all posts posted"""
        response = self.client.post('/api/V1/sales',data=json.dumps(products_data[0]),
            content_type='application/json')

        res=json.loads(response.data.decode())

        self.assertEqual(res['output'],'Sale record has been created')
        self.assertEqual(response.status_code, 201) 
        


    def test_get_all_sales(self):
        """These tests check all sales record """
        response=self.client.get('/api/V1/sales')

        res=json.loads(response.data.decode())
        self.assertEqual(res['output'],'These are your sales records')
        self.assertEqual(response.status_code,200)

    def test_get_one_sale(self):
        """These tests check  specific sales record """ 
        response = self.client.get('/api/V1/sales/1', content_type="application/json")
        self.assertTrue(response.status_code, 200)




    def test_wrong_id(self):
        """These tests when wrong id is entered"""
        sales_id = "a" 
        response = self.client.get('/api/V1/sales/' + sales_id)
        self.assertRaises(TypeError,response) 



   



    def test_nonexistant_sales_id(self):
        """Test check none existing sales_id """
        response = self.client.get('/api/V1/sales/20', content_type="application/json")
        self.assertEqual(response.status_code,404)



    













def teardown(self):
    self.app_context.pop()
