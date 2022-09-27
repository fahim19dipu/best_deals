# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:11:54 2022

@author: Fahim
"""

from bs4 import BeautifulSoup
import requests
import pyrebase 
######################################  scap mad chef website and update database
def scrap_upload_madchef():                       
    URL = "https://madchef.com.bd/menu"
    response = requests.get(URL)
    page_content = BeautifulSoup(response.content, "html.parser")
    c =0
    item = []
    all_products = []
    for i in range(100):
        tag = "menumodal"+str(i)
        try:
            table_body = page_content.find(id=tag)
            price = table_body.find('div', {'class': 'menumodal-price'}).text#.rstrip(' \n').replace('\n', '').replace('\r', '')
            title = table_body.find('div', {'class': 'menumodal-title'}).text
            cat = table_body.find('div', {'class': 'menumodal-category'}).text.replace("Category: ",'')
            desc = table_body.find('div', {'class': 'menumodal-description'}).text
               
            price = " ".join(price.split())
            price = int(price.replace('৳',''))
            
            title = " ".join(title.split())
            cat = " ".join(cat.split())
            desc = " ".join(desc.split())
            #print(title," ",price)
            all_products.append({
            "item_name": title,
            "description": desc,
            "price": price,
            "catagory": cat
            })
            temp = (title,price,cat,desc)
            item.append(temp)
            c+=1
        except:
            continue        
    print(all_products)
    
    URL = "https://madchef.com.bd/contact#branches"
    response = requests.get(URL)
    page_content = BeautifulSoup(response.content, "html.parser")
    table_body = page_content.find('div', {'class': 'row'})
    c =0
    item = []
    all_loaction= []
    table_body = table_body.find('div',{'class':"details"})
    table_body = table_body.find_all('div',{'class':"branch"})
    
    for i in range(len(table_body)):
        brach_name = table_body[i].find(class_="branch-name").text
        address = table_body[i].find(class_="branch-address").text
        phone = table_body[i].find(class_="branch-phone").text.replace('\u202d','').replace('\u202c','')  
        brach_name = " ".join(brach_name.split())
        address = " ".join(address.split())
        phone = " ".join(phone.split())
        all_loaction.append({
                "branch_name": brach_name,
                "address": address,
                "phone": phone,
                })
    print(all_loaction)
    ################################################   configure database
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
    ######################################################## Update database
    db.child("Database").child("Madchef").child("Menu").set(all_products)
    db.child("Database").child("Madchef").child("Locations").set(all_loaction)
#scrap_upload_madchef()
