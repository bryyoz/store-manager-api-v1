class User:
    '''Class represents operations related to products'''
    all_users = {}

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password


    def signup(self):
        new_user = dict(
            email = self.email,
            username = self.username,
            password = self.password
            )

        User.all_users.append(new_user)


    def get_one_user(self, email):

        for key in User.all_users:
            if key == email:
                return User.all_users[key]
        message = "User not found"
        return message