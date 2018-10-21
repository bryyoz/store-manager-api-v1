import unittest
from flask import json
from app import create_app

user_reg_data = [{"email": "kip@gmail.com",
                  "password": "1234",
                  "confirm_password": "1234"
                  }]
bad_user_reg_data =[{"email": "kip@gmail.com",
                      "password": "1234",
                      "confirm_password": "12345"
  
}]

user_login_data = [{"email": "kip@gmail.com",
                    "password": "1234"}]
bad_user_login = [{"email": "kip@gmail.com",
                   "password": "12345"}]

class TestAuthentication(unittest.TestCase):
    """Tests for user authentication"""

    def setUp(self):
        """Set up for configuration and testing env"""
        self.app = create_app('testing')
        self.app_context =self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

       
    
    def test_user_registration(self):
        """Test that user can register successfully"""
        user_reg = self.client.post('/api/V1/register',data=json.dumps(user_reg_data[0]),
          content_type='application/json')
        response = json.loads(user_reg.data.decode())
        self.assertEqual(response['message'], 'User created!')
        self.assertEqual(user_reg.status_code, 201)

    def test_existing_user(self):
        """Test that user cant register twice"""
        user_reg = self.client.post('/api/V1/register',data=json.dumps(user_reg_data[0]),
          content_type='application/json')
        response = json.loads(user_reg.data.decode())
        self.assertEqual(user_reg.status_code, 201)
        self.assertEqual(response['message'], 'User created!')
        
        user_reg1 = self.client.post('/api/V1/register',data=json.dumps(user_reg_data[0]),
          content_type='application/json')
        response1 = json.loads(user_reg1.data.decode())
        self.assertEqual(user_reg1.status_code, 202)
        self.assertEqual(response1['message'],'Email already exists.')

    def test_user_login(self):
        """Test that user can login"""
        
        user_login = self.client.post('/api/V1/login',data=json.dumps(user_login_data[0]),
          content_type='application/json')
        response = json.loads(user_login.data.decode())
        self.assertEqual(response['message'], 'Logged in successfully!')
        self.assertTrue(response['token'])
        self.assertEqual(user_login.status_code, 201)


    def test_user_login_incorrect_password(self):
        """Test that user cant login with incorrect password"""
        user_reg = self.client.post('/api/V1/register', data=json.dumps(user_reg_data[0]),
          content_type='application/json')
        response = json.loads(user_reg.data.decode())
        self.assertEqual(user_reg.status_code, 201)
        self.assertEqual(response['message'], 'User created!')
        user_login = self.client.post('/api/V1/login',data=json.dumps(bad_user_login[0]),
          content_type='application/json')
                                        
        response = json.loads(user_login.data.decode())
        self.assertEqual(response['message'], 'Invalid email or password. Please try again')
        self.assertEqual(user_login.status_code, 401)

    def test_login_no_pass(self):
        """Test that user cant login without password"""
        user_reg = self.client.post('/api/V1/register',data=json.dumps(user_reg_data[0]),
          content_type='application/json')
                                     
        response = json.loads(user_reg.data.decode())
        self.assertEqual(user_reg.status_code, 201)
        self.assertEqual(response['message'], 'User created!')

        user_login = self.client.post('/api/V1/login',data={"email": "kip@gmail.com"})
        response = json.loads(user_login.data.decode())
        self.assertEqual(response['message'], 'please enter your password')
        self.assertEqual(user_login.status_code, 401)

    def test_login_unregistered_account(self):
        user_login = self.client.post('/api/1/login',data={"email": "brian@mail.com",
          "password": "123409"})                            
        response = json.loads(user_login.data.decode())
        self.assertEqual(response['message'], 'email doesnt exist. Please register')
        self.assertEqual(user_login.status_code, 401)

   

   


    def tearDown(self):
        self.app_context.pop()