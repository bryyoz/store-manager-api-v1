from flask_bcrypt import Bcrypt
from Instance.config import Config
from functools import wraps
from flask import make_response, jsonify
from flask import request
from datetime import datetime, timedelta
import jwt



class User:
    '''Class represents operations related to products'''
    all_users = []
    
    def __init__(self, email, role, password, re_password):
        self.email = email
        self.role = role
        self.password = password
        self.re_password = re_password
        
        User.password = Bcrypt().generate_password_hash(password).decode()

    @classmethod
    def validate_user_password(cls, password):
        """Compare the user entered password and user registered password"""

        return Bcrypt().check_password_hash(User.password, password)
    


    def signup(self):
        
        new_user = dict(
            email = self.email,
            role = self.role,
            password = self.password,
            re_password = self.re_password

            )

        User.all_users.append(new_user)


    def get_one_user(self, email):
        one_user = [user for user in User.all_users if user['email'] == email]
        if one_user:
            return one_user
        return 'User not found'


    