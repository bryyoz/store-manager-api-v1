# store-manager-api-v1
[![Coverage Status](https://coveralls.io/repos/github/bryyoz/store-manager-api-v1/badge.svg)](https://coveralls.io/github/bryyoz/store-manager-api-v1)





This is a Store Manager Application
To Run and test this application
Take the following steps:
1. Create a virtual enviroment with the command `$ virtualenv venv --distribute`
2. Activate the virtual enviroment with the command `$ source venv/scripts/activate
3. Ensure you have installed GIT
4. Clone the repository i.e `$ git clone https://github.com/bryyoz/store-manager-api-v1.git
5. Install requirements `$ pip install -r requirements.txt`
After completing the following, it is time to run the app
i) To run the tests use `$ pytest -v`
ii) To run the app use python run.py


The following endpoints should be working
1. GET /products	Fetch all products
2. GET /products/	Fetch a single product record
3. GET /sales	Fetch all sale records
4. GET /sales/	Fetch a single sale record
5. POST /products	Create a product
6. POST /sales	Create a sale order
7. POST /auth/signup	Signup a user
8. POST /auth/login	Login a user