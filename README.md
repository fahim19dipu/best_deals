# best_deals
A python REST API that provides best deals for given item name, prefered price and location.
## Description
This project is a REST API based on python flask. It provides best deal for a certain food item based on users location and prefered price using data model and scrapping.

It scraps the websites of "Mad Chef" and "Pizza hut", two of the most popular food chains in bangladesh and stores their location, menu, prices, and offers and updates then in a Firebase realtime database. Then it runs a flask server to listen for ```get requests```. From there based on user request a data models finds all menu items which matches with the user request and whose prices are with in +-10% of the prefered price. The it calculates user location with all locations of both food chains and finds two nearest branch of each resturant. Then the API responds to the ```get request``` with ```json response```containing matched food items, nearest mad chef locations and nearest pizzahut locations.
## How to Install and Run the Project
The modules being used here are beautifulsoup4==4.11.1, Flask==1.1.2, Flask_RESTful==0.3.8, numpy==1.23.1, pyrebase==3.0.27, Pyrebase4==4.5.0, requests==2.28.1, selenium==3.141.0. They are also mentioned in the requirement.txt file. they can be installed manually or using pip command.
```python
pip install requirement.txt
```
To run the API run only the flask_api_main.py file from src folder in python. It will scarap the data and update the database. Then it will run the REST API and it will wait for htttp requests where "http://127.0.0.1:5000/best_deals/" is the root-endpoint and ":item/:pref_price/:location" is the path". in the path "item" must be a string, "pref_price" must be integer denoting the prefered price, "location" must be a string denoting the address of the users.
after getting a correct request the API will send a JSON response containing matched food items, nearest mad chef locations and nearest pizzahut location which can be accessed respectively as ```response.item_list```, ```response.madChef_loaction``` and ```response.pizzahut_locations``. Each of which is a list of dictionary.
## Input
```html
http://127.0.0.1:5000/best_deals/chicken/400/banani
```
## Output
```json
{
    "item_list": [
        {
            "catagory": "Crispy Chicken",
            "description": "Original chicken wings/ Bangkok style fried chicken.",
            "item_name": "Original",
            "price": 399,
            "resturant": "Mad Chef"
        },
        {
            "catagory": "Crispy Chicken",
            "description": "Chicken wings/ Bangkok style fried chicken dipped in hot sweet & sour pepper sauce.",
            "item_name": "Buffalo",
            "price": 399,
            "resturant": "Mad Chef"
        },
        .........
    ],
    "madChef_loaction": [
        {
            "address": "5th Floor, House 47 Road 11, Block H Dhaka - 1213.",
            "branch_name": "Banani",
            "phone": "+880 17 4996 0363",
            "distance": 0.4
        },
        {
            "address": "Serves: Gulshan, Badda, Niketan, Mohakhali, Shahjadpur",
            "branch_name": "Gulshan (Delivery)",
            "phone": "+880 13 1219 5220",
            "distance": 3.1
        }
    ],
    "pizzahut_locations": [
        {
            "address": "Plot- 50, Road- 11, Block- C, Banani Police Station, Banani, Dhaka-1213. ",
            "branch_name": "Pizza Hut Delivery Banani",
            "phone": " 9858272, 9858274, 09613999777",
            "distance": 0.9
        },
        {
            "address": "1st Floor, House:12/B, Road:55, Gulshan-2, Near Gulshan Police Station. ",
            "branch_name": "Pizza Hut FCD Gulshan 2",
            "phone": " 09613772233",
            "distance": 1.0
        }
    ]
}
```
