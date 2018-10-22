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
        admin_signup = self.test_client.post("/api/V1/register",data=self.user_admin, headers={
                'content-type': 'application/json'})
        self.user_attendant = json.dumps({
                "name": "loise",
                "email": "loise@gmail.com",
                "password": "1234",
                "role": "attendant"
            })

        attendant_signup = self.test_client.post("/api/V1/register",data=self.user_attendant,
                headers={'content-type': 'application/json'})
        self.login_admin = json.dumps({
            "email": "brian@gmail.com",
            "password": "1234"
        })

        admin_login = self.test_client.post("/api/V1/login",data=self.login_admin, headers={
                                                'content-type': 'application/json' })
        #self.token_for_admin = json.loads(admin_login.data.decode())["token"]
        self.login_attendant = json.dumps({
            "email": "brian@gmail.com",
            "password": "brian"
        })

        attendant_login = self.test_client.post("/api/V1/login", data=self.login_attendant,
                                                headers={
                                                    'content-type': 'application/json'
                                                })
        #self.token_for_attendant = json.loads(attendant_login.data.decode())["token"]



    
    def test_user_not_exist(self):
        """Test that user can login"""
        
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