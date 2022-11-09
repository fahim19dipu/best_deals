# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 23:00:52 2022

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 18:14:14 2022

@author: user
"""

import pyrebase 
import distance_calculator 
import numpy as np
def model(pref_price,item,location):
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

    menu_mad =db.child("Database").child("Madchef").child("Menu").get()
    menu_hut = db.child("Database").child("pizzahut").child("Menu").get()
    loc_mad =db.child("Database").child("Madchef").child("Locations").get()
    loc_hut = db.child("Database").child("pizzahut").child("Locations").get()  
    ###################################    Find items  at around 20% varience of the prefered price
    matched_items = []
    available_at_mad = 0
    available_at_hut = 0
    ###################################    Find items at mad chef
    for data_item in menu_mad.each(): 
        data =data_item.val() 
        if data["price"] <= int(pref_price*1.1) and data["price"] >= int(pref_price*.9):
            if item.lower() in data["item_name"].lower() or item.lower() in data["catagory"].lower() or item.lower() in data["description"].lower():
                #print(f"{data['item name']} {data['catagory']} {data['price']}")
                data.update({"resturant": "Mad Chef" })
                matched_items.append(data)
                available_at_mad+=1
    #print(available_at_mad)   
    ##################################    Find items at pizzahut   
    for data_item in menu_hut.each(): 
        data =data_item.val() 
        if data["price"] <= int(pref_price*1.1) and data["price"] >= int(pref_price*.9):
            if item.lower() in data["item_name"].lower() or item.lower() in data["catagory"].lower() or item.lower() in data["description"].lower():
                #print(f"{data['item name']} {data['catagory']} {data['price']}")
                data.update({"resturant": "Pizza Hut" })
                matched_items.append(data)
                available_at_hut+=1
                
    #print(matched_items)         
    #print(available_at_hut)  
    #################################     Find 2 nearest madchef locations if item found at madchef menu
    nearest_mad= []
    address_mad = []
    loc_list_mad =[]
    if available_at_mad>=1:
        for data in loc_mad.each(): 
            loc =data.val()
            address_mad.append(loc['address'])
            loc_list_mad.append(loc)
            
        distances = np.array(distance_calculator.calc_distance(location, address_mad))
        indx = np.argpartition(distances,2)
        indx = indx[0:2]
        
        for i in indx:
            loc_list_mad[i].update({"distance": distances[i] })
            nearest_mad.append(loc_list_mad[i])
        #print(nearest_mad)
    #################################     Find 2 nearest pizzahut locations if item found at pizzahut menu        
    nearest_hut =[]
    address_hut = []    
    loc_list_hut =[]
    if available_at_hut>=1:
        for data in loc_hut.each(): 
            loc =data.val()
            address_hut.append(loc['address'])
            loc_list_hut.append(loc)
            
            
        distances = np.array(distance_calculator.calc_distance(location, address_hut))
        indx = np.argpartition(distances,2)
        indx = indx[0:2]
        
        for i in indx:
            loc_list_hut[i].update({"distance": distances[i] })
            nearest_hut.append(loc_list_hut[i])
        #print(nearest_hut)
        ###############################
    results = {"item_list":matched_items,"madChef_loaction":nearest_mad,"pizzahut_locations":nearest_hut}
    return results
        
# pref_price = 400
# item = "burger"
# location = "uttara"
# #model(pref_price,item,location)