# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 00:58:17 2022

@author: user
"""

from bs4 import BeautifulSoup
import requests
import pyrebase 

def scrap_upload_madchef():
    URL = "https://madchef.com.bd/#menu"
    response = requests.get(URL)
    page_content = BeautifulSoup(response.content, "html.parser")
    
    all_products = []
    titles =[s  for div in page_content.select('.modal-footer .modal-title') for s in div.stripped_strings]     
    price =[int(s.replace("Tk ",''))  for div in page_content.select('.modal-footer .modal-price') for s in div.stripped_strings]
    catagory =[s.replace("Category: ",'')  for div in page_content.select('.modal-footer .modal-category') for s in div.stripped_strings]
    description = [s  for div in page_content.select('.modal-footer .modal-details') for s in div.stripped_strings]
    for i in range(len(titles)):
        all_products.append({
        "item_name": titles[i],
        "description": description[i],
        "price": price[i],
        "catagory": catagory[i]
        })
    print(all_products)
    
    all_location = []
    branch =[s  for div in page_content.select('.location-information-box .branch-name') for s in div.stripped_strings]     
    address =[s  for div in page_content.select('.location-information-box .address') for s in div.stripped_strings]
    phone =[s.replace('\u202d','').replace('\u202c','') for div in page_content.select('.location-information-box .phone') for s in div.stripped_strings]
    for i in range(len(branch)):
        all_location.append({
        "branch_name": branch[i],
        "address": address[i],
        "phone": phone[i]
        })
    print(all_location)   
    
    firebaseConfig = {
      "apiKey": "AIzaSyAeJ-M2zzxApfppZnATuwqyp0CL90xWwJk",
      "authDomain": "fast-food-chains.firebaseapp.com",
      "databaseURL": "https://fast-food-chains-default-rtdb.asia-southeast1.firebasedatabase.app",
      "projectId": "fast-food-chains",
      "storageBucket": "fast-food-chains.appspot.com",
      "messagingSenderId": "215475941504",
      "appId": "1:215475941504:web:9f712eebedbaa6626f3665",
      "measurementId": "G-2BSE357B7V"
    }
    
    firebase=pyrebase.initialize_app(firebaseConfig)
    db= firebase.database()
    
    db.child("Database").child("Madchef").child("Menu").set(all_products)
    db.child("Database").child("Madchef").child("Locations").set(all_location)    
#scrap_upload_madchef()