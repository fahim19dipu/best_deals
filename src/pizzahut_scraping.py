# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 01:16:22 2022

@author: Fahim
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re 
import time
from selenium.webdriver.chrome.options import Options
import pyrebase 
####################################### scrap pizzahut and update database
def scrap_upload_pizzahut():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    #chrome_options.add_argument("--disable-gpu")
    #chrome_options.add_argument("--no-sandbox") # linux only
    chrome_options.add_argument("--headless")
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    # chrome_options.headless = True # also works
    
    driver = webdriver.Chrome('C:/Users/user/Desktop/chromedriver_win32/chromedriver',options=chrome_options)
    
    url = 'https://www.pizzahutbd.com/'
    driver.get(url)
    print(driver.title)
    ###############################################   main page
    inputElement = driver.find_element_by_xpath('//*[@id="delivery"]/div/a/div/input')
    inputElement.click()
    #############################################  pop up
    inputElement = driver.find_element_by_id("pac-input")
    driver.implicitly_wait(5)
    inputElement.send_keys('Dhaka Bangladesh')
    time.sleep(5) 
    inputElement.send_keys(Keys.ARROW_DOWN)
    inputElement.send_keys(Keys.ENTER)
    time.sleep(3) 
    ############################################# 
    #print(driver.title)
    all_product = []
    pan_pizza=[]
    cheesy_bites=[]
    sussage_crust=[]
    thin_crust=[]
    pasta=[]
    appatizers =[]
    drinks =[]
    drinks =[]
    ############################################### pan pizza page
    items  = [i.text for i in driver.find_elements_by_class_name("left-con-pizzas")]
    print(driver.title)
    price  = [i.text for i in driver.find_elements_by_class_name("price-info")]
    price= [re.sub('[^\d\.]', '', price[i]) for i in range(len(price))]
    desc = [i.text for i in driver.find_elements_by_class_name("short_desc")]
    
    for  i in range(len(items)):
            pan_pizza.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": "pan pizza"
            })
            all_product.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": "pan pizza"
            })
    print(len(pan_pizza))
    #all_product.append(pan_pizza)
    ############################################## cheesy bites pizza tab
    inputElement = driver.find_element_by_xpath('//*[@id="pnProductNavContents"]/a[2]').click()
    items  = [i.text for i in driver.find_elements_by_class_name("left-con-pizzas")]
    price  = [i.text for i in driver.find_elements_by_class_name("price-info")]
    price= [re.sub('[^\d\.]', '', price[i]) for i in range(len(price))]
    desc = [i.text for i in driver.find_elements_by_class_name("short_desc")]
    
    for  i in range(len(items)):
            cheesy_bites.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": "cheesy bites pizza"
            })
            all_product.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": "cheesy bites pizza"
            })
    print(len(cheesy_bites))
    #all_product.append(cheesy_bites)
    ########################################## saussage crust pizza tab
    inputElement = driver.find_element_by_xpath('//*[@id="pnProductNavContents"]/a[3]').click()
    items  = [i.text for i in driver.find_elements_by_class_name("left-con-pizzas")]
    price  = [i.text for i in driver.find_elements_by_class_name("price-info")]
    price= [re.sub('[^\d\.]', '', price[i]) for i in range(len(price))]
    desc = [i.text for i in driver.find_elements_by_class_name("short_desc")]
    
    for  i in range(len(items)):
            sussage_crust.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": "saussage crust pizza"
            })
            all_product.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": "saussage crust pizza"
            })
    print(len(sussage_crust))
    #all_product.append(sussage_crust)
    ############################################ thin crust pizza tab
    inputElement = driver.find_element_by_xpath('//*[@id="pnProductNavContents"]/a[4]').click()
    items  = [i.text for i in driver.find_elements_by_class_name("left-con-pizzas")]
    price  = [i.text for i in driver.find_elements_by_class_name("price-info")]
    price= [re.sub('[^\d\.]', '', price[i]) for i in range(len(price))]
    desc = [i.text for i in driver.find_elements_by_class_name("short_desc")]
    
    for  i in range(len(items)):
            thin_crust.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": "Thin crust pizza"
            })
            all_product.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": "Thin crust pizza"
            })
    print(len(thin_crust))
    #all_product.append(thin_crust)
    ##########################################   pasta page
    inputElement = driver.find_element_by_xpath('//*[@id="navbar"]/ul/li[2]/a').click()
    items  = [i.text for i in driver.find_elements_by_class_name("left-con-pizzas")]
    price  = [i.text for i in driver.find_elements_by_class_name("price-info")]
    price= [re.sub('[^\d\.]', '', price[i]) for i in range(len(price))]
    desc = [i.text for i in driver.find_elements_by_class_name("short_desc")]
    for  i in range(len(items)):
            pasta.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": "pasta"
            })
            all_product.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": "pasta"
            })
    print(len(pasta))
    #all_product.append(pasta)
    ###########################################   appatizers page
    inputElement = driver.find_element_by_xpath('//*[@id="navbar"]/ul/li[3]/a').click()
    items  = [i.text for i in driver.find_elements_by_class_name("left-con-pizzas")]
    price  = [i.text for i in driver.find_elements_by_class_name("pro_price")]
    price = ' '.join(price).split()
    #price= [re.sub('[^\d\.]', '', price[i]) for i in range(len(price))]
    desc = [i.text for i in driver.find_elements_by_class_name("short_desc")]
    
    for  i in range(len(items)):
            appatizers.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": "appatizers"
            })
            all_product.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": "appatizers"
            })        
    print(len(appatizers))
    #all_product.append(appatizers)
    ###################################    drinks page
    inputElement = driver.find_element_by_xpath('//*[@id="navbar"]/ul/li[5]/a').click()
    items  = [i.text for i in driver.find_elements_by_class_name("left-con-pizzas")]
    price  = [i.text for i in driver.find_elements_by_class_name("pro_price")]
    #price= [re.sub('[^\d\.]', '', price[i]) for i in range(len(price))]
    price = ' '.join(price).split()
    desc = [i.text for i in driver.find_elements_by_class_name("short_desc")]
    
    for  i in range(len(items)):
            drinks.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": "Drinks"
            })
            all_product.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": "Drinks"
            })
    print(len(drinks))
    
    ################################## deals page
    deals = []
    inputElement = driver.find_element_by_xpath('//*[@id="navbar"]/ul/li[4]/a').click()
    inputElement = driver.find_elements_by_class_name("deals_card")
    for el in inputElement:
        items  = el.find_element_by_class_name("deal-item-name")
        #print(items.text)
        try:
            price  = el.find_element_by_class_name("pro_price").text
            #price = ' '.join(price).split()
        except:
            price = "0"
        #print(price)

        #price= [re.sub('[^\d\.]', '', price[i]) for i in range(len(price))]
        
        desc =  el.find_element_by_class_name("deal-item-desc")
    
        deals.append({
            "item_name": items.text,
            "description": desc.text,
            "price": int(price),
            "catagory": "deal"
            })
        all_product.append({
            "item_name": items.text,
            "description": desc.text,
            "price": int(price),
            "catagory": "deal"
            })
    print(len(deals))
    #######################################   location page
    driver.get("https://www.pizzahutbd.com/store-filter")
    name  = [i.text for i in driver.find_elements_by_class_name("storename")]
    address  = [i.text for i in driver.find_elements_by_class_name("storeaddress")]
    contact = address[1::2]
    contact = [contact[i].replace("Contact Number:","") for i in range(len(contact))]
    address = address[0::2]
    address = [i.split("Contact",1)[0] for i in address]
    all_loaction =[]
    for i in range(len(name)):
        all_loaction.append({
                "branch_name": name[i],
                "address": address[i],
                "phone": contact[i],
                })
    
    #print(all_loaction)
    #print(all_product)
    #print(len(all_product))
    #print(all_loaction)
    driver.quit()
    ######################################## database config
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
    ####################################### update database
    db.child("Database").child("pizzahut").child("Menu").set(all_product)
    db.child("Database").child("pizzahut").child("Locations").set(all_loaction)
#scrap_upload_pizzahut()
