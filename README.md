# Ecommerce Module and Infinite Scroll
Live server ==> http://mahmud2.pythonanywhere.com/
## API List
### Login & verify user:
| SRL | METHOD | ROUTE | FUNCTIONALITY | FIELDS | ACCESS |
| ------- | ------- | ----- | ------------- | ------------- | ------------- |
| *1* | *POST* | ```/api/token/``` | _Login user_| _**username**, **password**_|_All users_|
| *2* | *POST* | ```/api/token/refresh/ ``` | _Refresh the access token_|_**token**_|_Allow any_|
| *3* | *POST* | ```/api/token/verify/``` | _Verify the token_|_**token**_|_Allow any_|
-----------------------------

### User related API:
* When user is created, by default the user will be buyer.
* To add seller, only admin will make the existing user as a seller.

| SRL | METHOD | ROUTE | FUNCTIONALITY | FIELDS | ACCESS |
| ------- | ------- | ----- | ------------- | ------------- | ------------- |
| *4* | *POST* | ```/api/auth/user/``` | _Create new user_| _**username**, **password**,first_name, last_name, email._|_Allow any_|
| *5* | *GET* | ```/api/auth/user/ ``` | _Get all user list_|_id, username, email,  first_name, last_name_|_Admin_|
| *6* | *PATCH* | ```/api/auth/user/id/``` | _Update user details_|_username, email,  first_name, last_name_|_Admin_|
| *7* | *DELETE* | ```/api/auth/user/id/``` | _Delete user_|_None_|_Admin_|
-----------------------------

### Product related API:
* Anyone can view the products.
* Only seller and admin can add, edit, update and delete the product.

| SRL | METHOD | ROUTE | FUNCTIONALITY | FIELDS | ACCESS |
| ------- | ------- | ----- | ------------- | ------------- | ------------- |
| *8* | *POST* | ```/api/product/``` | _Create new product_| _title, description, seller(auto add), price, quantity, image._|_Seller, Admin_|
| *9* | *GET* | ```/api/product/ ``` | _Get all product list_|_title, description, price, quantity, image, seller, created_at, updated_at._|_Allow any_|
| *10* | *PATCH* | ```/api/product/id/``` | _Update product details_|_title, description, price, quantity, image_|_Seller, Admin_|
| *11* | *DELETE* | ```/api/product/id/``` | _Delete  product_|_None_|_Seller, Admin_|
-----------------------------

### Cart and CartItem related API:
* Each user has a cart which is created automatically when the user is created.
* I have used **signals** for creating cart automatically.
* Only authenticated user can add, edit, update and delete the cart item.

| SRL | METHOD | ROUTE | FUNCTIONALITY | FIELDS | ACCESS |
| ------- | ------- | ----- | ------------- | ------------- | ------------- |
| *12* | *POST* | ```/api/cartitem/``` | _Create new cart item._| _**product_id**, quantity._|_Authenticated_|
| *13* | *GET* | ```/api/cartitem/ ``` | _Get all cart items for authenticated user_|_id, cart, product_id, quantity, price_|_Authenticated_|
| *14* | *PATCH* | ```/api/cartitem/id/``` | _Update cart item_|_product_id, quantity_|_Authenticated_|
| *15* | *DELETE* | ```/api/cartitem/id/``` | _Delete  cart item_|_None_|_Authenticated_|
-----------------------------

### Order related API:
* Order will be created if cart item is available. 
* If cart is empty, order not created and will show error messages==> **{'error': 'Cart is empty. Please add items to the cart before placing an order'}**

| SRL | METHOD | ROUTE | FUNCTIONALITY | FIELDS | ACCESS |
| ------- | ------- | ----- | ------------- | ------------- | ------------- |
| *16* | *POST* | ```/api/order/``` | _Create new order._| _none_|_Authenticated_|
| *17* | *GET* | ```/api/order/ ``` | _Get all order list with items for authenticated user_|_id, total_price, status, items [id, product, quantity, price]_|_Authenticated_|
-----------------------------

# Setup
The first thing to do is to clone the repository:
```sh
$ https://github.com/MahmudJewel/drf-ecommerce-module
```

Create a virtual environment to install dependencies in and activate it:
```sh
$ cd drf-ecommerce-module
$ python -m venv venv
$ source venv/bin/activate
```
Then install the dependencies:
```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies

Then configured celery in your device for auto collect daily revenue.

# Tools
### Back-end
#### Language:
	Python

#### Frameworks:
	Django 
    Django Rest Framework
	
#### Other libraries / tools:
	Celery
    django-celery-beat
    django-celery-results 
    Redis
    djangorestframework-simplejwt
    django-htmx

### Happy Coding

