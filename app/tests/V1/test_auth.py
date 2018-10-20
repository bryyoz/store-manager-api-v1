import unittest
from flask import json
from app import create_app


class TestAuthentication(unittest.TestCase):
    """Tests for user authentication"""

    def setUp(self):
        """Set up for configuration and testing env"""
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client

        self.sample_user_reg_data = {
                                    "email": "mail@mail.com",
                                    "password": "pass",
                                    "confirm_password": "pass"}

        self.sample_user_reg_bad = {
                                    "email": "mail@mail.com",
                                    "password": "pass",
                                    "confirm_password": "bad_pass"}

        self.sample_user_login_data = {
                                      "email": "mail@mail.com",
                                      "password": "pass"}
        self.sample_user_login_bad = {
                                      "email": "mail@mail.com",
                                      "password": "bad_pass"}
    
    def test_user_registration(self):
        """Test that user can register successfully"""
        user_reg = self.client().post('/api/V1/register',
                                      data={
                                           "email": "user@mail.com",
                                           "password": "pass",
                                           "confirm_password": "pass"})
        response = json.loads(user_reg.data.decode())
        self.assertEqual(response['message'], "User created!")
        self.assertEqual(user_reg.status_code, 201)

    def test_existing_user(self):
        """Test that user cant register twice"""
        user_reg = self.client().post('/api/V1/register',
                                      data=self.sample_user_reg_data)
        response = json.loads(user_reg.data.decode())
        self.assertEqual(user_reg.status_code, 201)
        self.assertEqual(response['message'], "User created!")
        
        user_reg1 = self.client().post('/api/V1/register',
                                      data=self.sample_user_reg_data)
        response1 = json.loads(user_reg1.data.decode())
        self.assertEqual(user_reg1.status_code, 202)
        self.assertEqual(response1['message'],'Email already exists.')

    def test_user_login(self):
        """Test that user can login"""
        
        user_login = self.client().post('/api/V1/login',
                                        data={
                                           "email": "user1@mail.com",
                                           "password": "pass"})
        response = json.loads(user_login.data.decode())
        self.assertEqual(response['message'], 'Logged in successfully!')
        self.assertTrue(response['token'])
        self.assertEqual(user_login.status_code, 201)

   

    def test_login_unregistered_account(self):
        user_login = self.client().post('/api/V1/login',
                                        data={
                                           "email": "user4@mail.com",
                                           "password": "pass"})
        response = json.loads(user_login.data.decode())
        self.assertEqual(response['message'], "Your account does not exist!, Please Register!")
        self.assertEqual(user_login.status_code, 401)

    def test_invalid_email(self):
        """Test that user cant use invalid email"""
        user_reg = self.client().post('/api/V1/register',
                                      data={
                                           "email": "nerd.com",
                                           "password": "pass",
                                           "confirm_password": "pass"})
        response = json.loads(user_reg.data.decode())
        self.assertEqual(user_reg.status_code, 400)
        self.assertEqual(response['message'], 'enter a valid email')
        user_login = self.client().post('/api/V1/login',
                                        data={
                                           "email": "nerd.com",
                                           "password": "bad_pass"})
        response = json.loads(user_login.data.decode())
        self.assertEqual(response['message'], "Your account does not exist!, Please Register!")
        self.assertEqual(user_login.status_code, 401)

    def tearDown(self):
        del self.sample_user_login_bad
        del self.sample_user_login_data
        del self.sample_user_reg_bad
        del self.sample_user_reg_data