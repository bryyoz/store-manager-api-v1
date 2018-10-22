from flask_bcrypt import Bcrypt

class User:
    '''Class represents operations related to products'''
    all_users = []

    def __init__(self, email, username, password):
        self.email = email
        User.password = Bcrypt().generate_password_hash(password).decode()

    @classmethod
    def validate_user_password(cls, password):
        """Compare the user entered password and user registered password"""

        return Bcrypt().check_password_hash(User.password, password)


    def signup(self):
        payload = dict(
            email = self.email,
            password = self.password
            )

        User.all_users.append(payload)


    def get_one_user(self, email):

        one_user = [user for user in User.all_users if user['email'] == email]
        if one_user:
            return one_user
        return 'User not found'