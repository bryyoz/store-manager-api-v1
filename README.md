# store-manager-api-v1
[![Coverage Status](https://coveralls.io/repos/github/bryyoz/store-manager-api-v1/badge.svg)](https://coveralls.io/github/bryyoz/store-manager-api-v1)
[![Maintainability](https://api.codeclimate.com/v1/badges/b0a7e0e967007232b6db/maintainability)](https://codeclimate.com/github/bryyoz/store-manager-api-v1/maintainability)
[![Build Status](https://travis-ci.org/bryyoz/store-manager-api-v1.svg?branch=develop)](https://travis-ci.org/bryyoz/store-manager-api-v1)


**Store Manager**

Store Manager is a web application that helps store owners manage sales and product inventory 
records. This application is meant for use in a single store. 


**Code style**

The api is constructed using python flask and flask restplus

Testing is done using pytest

Test coverage is done using pytest-cov

**Installation**

Clone the repo to your local machine.

open using python run run.py

open localhost

**Features**

1. Store attendant can search and add products to buyer’s cart. 
2. Store attendant can see his/her sale records but can’t modify them. 
3. App should show available products, quantity and price. 
4. Store owner can see sales and can filter by attendants. 
5. Store owner can add, modify and delete products.
6. Store owner can give admin rights to a store attendant. 
7. Products should have categories. 
8. Store attendants should be able to add products to specific categories. 

**EndPoint Functionality**
1. GET /products  			Fetch all products  Get all available products. 
2. GET /products/productId  Fetch a single product record  
3. GET /sales  				Fetch all sale records  Get all sale records.
4. GET /sales/saleId  		Fetch a single sale record  
5. POST /products  			Create a product
6. POST /sales  			Create a sale order

**Authors**
Brian Ngeno

