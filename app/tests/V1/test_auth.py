import unittest
from flask import json
from app import create_app

class TestAuthentication(unittest.TestCase):
    """Tests for user authentication"""

    def setUp(self):
        """Set up for configuration and testing env"""
        self.app = create_app('testing')
        self.test_client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.client = self.app.test_client()

        self.user_admin = json.dumps({
            "name": "brian",
            "email": "brian@gmail.com",
            "password": "1234",
            "role": "admin"
        })

        self.user_attendant = json.dumps({
                "name": "loise",
                "email": "loise@gmail.com",
                "password": "1234",
                "re_password":"1234",
                "role": "attendant"
            })
        
        self.login_admin = json.dumps({
            "email": "brian@gmail.com",
            "password": "1234"
        })
        
        self.login_attendant = json.dumps({
            "email": "loise@gmail.com",
            "password": "1234"
        })

       


    def test_sign_up_user(self):
       
        new_user = self.client.post('/api/V1/register', data=self.user_attendant, 
            content_type='application/json')
        result = json.loads(new_user.data.decode())
        self.assertEqual(result["message"], "User created!")
        self.assertEqual(new_user.status_code, 201)
        

    def test_user_login(self):
        """Test that user can login"""
        
        user_attendant_login = self.client.post('/api/V1/login',data=self.login_attendant,
          content_type = 'application/json') 
        response = json.loads(user_attendant_login.data.decode())
        self.assertEqual(response['message'], 'Logged in successfully!')
        self.assertEqual(user_attendant_login.status_code, 201)
        self.token_attendant = json.loads(user_attendant_login.data.decode()).get("x-api-key")
        

    
    def test_user_not_exist(self):
        
        user_login = self.client.post('/api/V1/login',data=self.login_admin,
          headers={'content-type': 'application/json'}) 
        response = json.loads(user_login.data.decode())
        self.assertEqual(response['message'], 'Your account does not exist!, Please Register!')
        self.assertEqual(user_login.status_code, 401)


    def test_user_login_none_existing_password(self):
        """Test that user cant login with incorrect password"""
        a_login = self.client.post('/api/V1/login',data=json.dumps({
          "email": "brian@gmail.com",
            "password": "1234"}),
          headers={'content-type': 'application/json'}) 
                                        
        response = json.loads(a_login.data.decode())
        self.assertEqual(response['message'], 'Your account does not exist!, Please Register!')
        self.assertEqual(a_login.status_code, 401)
   


    def tearDown(self):
        pass