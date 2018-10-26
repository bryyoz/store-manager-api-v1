import unittest


import sys # fix import errors
import os
#sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import create_app
import json




class TestClient(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context =self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()


        self.sales_record = json.dumps({
            "email": "brian@gmail.com",
            "password": "1234"})

        

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
    
    def test_post_sales(self):
        """These tests check for all posts posted"""

        self.user_authentication_register()

        response = self.user_authentication_login()

        token_admin = json.loads(response.data.decode()).get("x-api-key")
        result = self.client.post('/api/V1/sales', headers=dict(Authorization ="Bearer {}".format(token_admin)),
            data=json.dumps({
            "names":"josh kie",
            "cart":50,
            "total_price":2345}),content_type='application/json')

        res=json.loads(result.data.decode())

        self.assertEqual(res['output'],'Sale record has been created')
        self.assertEqual(response.status_code, 201) 
        
    



    def test_get_all_sales(self):
        """These tests check all sales record """

        self.user_authentication_register()
        
        response = self.user_authentication_login()

        token_admin = json.loads(response.data.decode()).get("x-api-key")
        response=self.client.get('/api/V1/sales', headers=dict(Authorization ="Bearer {}".format(token_admin)))

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


  



    













def teardown(self):
    self.app_context.pop()
