# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 01:16:22 2022

@author: user
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re 
import time
from selenium.webdriver.chrome.options import Options
def scrap_upload_pizzahut():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    #chrome_options.add_argument("--disable-gpu")
    #chrome_options.add_argument("--no-sandbox") # linux only
    #chrome_options.add_argument("--headless")
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    # chrome_options.headless = True # also works
    
    driver = webdriver.Chrome('C:/Users/user/Desktop/chromedriver_win32/chromedriver',options=chrome_options)
    
    url = 'https://www.pizzahutbd.com/'
    driver.get(url)
    print(driver.title)
    
    inputElement = driver.find_element_by_xpath('//*[@id="delivery"]/div/a/div/input')
    inputElement.click()
    inputElement = driver.find_element_by_id("pac-input")
    driver.implicitly_wait(7)
    inputElement.send_keys('Dhaka Bangladesh')
    time.sleep(5) 
    inputElement.send_keys(Keys.ARROW_DOWN)
    inputElement.send_keys(Keys.ENTER)
    time.sleep(3) 
    print(driver.title)
    all_product = []
    pan_pizza=[]
    cheesy_bites=[]
    sussage_crust=[]
    thin_crust=[]
    pasta=[]
    appatizers =[]
    drinks =[]
    drinks =[]
    ##################################################################
    items  = [i.text for i in driver.find_elements_by_class_name("left-con-pizzas")]
    print(driver.title)
    price  = [i.text for i in driver.find_elements_by_class_name("price-info")]
    price= [re.sub('[^\d\.]', '', price[i]) for i in range(len(price))]
    desc = [i.text for i in driver.find_elements_by_class_name("short_desc")]
    cat = [i.text for i in driver.find_elements_by_xpath('//*[@id="pnProductNavContents"]/a[1]')]
    cat = cat[0]
    for  i in range(len(items)):
            pan_pizza.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": cat
            })
            all_product.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": cat
            })
    print(len(pan_pizza))
    #all_product.append(pan_pizza)
    ######################################################################
    inputElement = driver.find_element_by_xpath('//*[@id="pnProductNavContents"]/a[2]').click()
    items  = [i.text for i in driver.find_elements_by_class_name("left-con-pizzas")]
    price  = [i.text for i in driver.find_elements_by_class_name("price-info")]
    price= [re.sub('[^\d\.]', '', price[i]) for i in range(len(price))]
    desc = [i.text for i in driver.find_elements_by_class_name("short_desc")]
    cat = [i.text for i in driver.find_elements_by_xpath('//*[@id="pnProductNavContents"]/a[2]')]
    cat = cat[0]
    for  i in range(len(items)):
            cheesy_bites.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": cat
            })
            all_product.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": cat
            })
    print(len(cheesy_bites))
    #all_product.append(cheesy_bites)
    #######################################################################
    inputElement = driver.find_element_by_xpath('//*[@id="pnProductNavContents"]/a[3]').click()
    items  = [i.text for i in driver.find_elements_by_class_name("left-con-pizzas")]
    price  = [i.text for i in driver.find_elements_by_class_name("price-info")]
    price= [re.sub('[^\d\.]', '', price[i]) for i in range(len(price))]
    desc = [i.text for i in driver.find_elements_by_class_name("short_desc")]
    cat = [i.text for i in driver.find_elements_by_xpath('//*[@id="pnProductNavContents"]/a[3]')]
    cat = cat[0]
    for  i in range(len(items)):
            sussage_crust.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": cat
            })
            all_product.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": cat
            })
    print(len(sussage_crust))
    #all_product.append(sussage_crust)
    ##########################################################################
    inputElement = driver.find_element_by_xpath('//*[@id="pnProductNavContents"]/a[4]').click()
    items  = [i.text for i in driver.find_elements_by_class_name("left-con-pizzas")]
    price  = [i.text for i in driver.find_elements_by_class_name("price-info")]
    price= [re.sub('[^\d\.]', '', price[i]) for i in range(len(price))]
    desc = [i.text for i in driver.find_elements_by_class_name("short_desc")]
    cat = [i.text for i in driver.find_elements_by_xpath('//*[@id="pnProductNavContents"]/a[4]')]
    cat = cat[0]
    for  i in range(len(items)):
            thin_crust.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": cat
            })
            all_product.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": cat
            })
    print(len(thin_crust))
    #all_product.append(thin_crust)
    ################################################################################
    inputElement = driver.find_element_by_xpath('//*[@id="navbar"]/ul/li[2]/a').click()
    items  = [i.text for i in driver.find_elements_by_class_name("left-con-pizzas")]
    price  = [i.text for i in driver.find_elements_by_class_name("price-info")]
    price= [re.sub('[^\d\.]', '', price[i]) for i in range(len(price))]
    desc = [i.text for i in driver.find_elements_by_class_name("short_desc")]
    cat = [i.text for i in driver.find_elements_by_xpath('//*[@id="navbar"]/ul/li[2]/a')]
    cat = cat[0]
    for  i in range(len(items)):
            pasta.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": cat
            })
            all_product.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": cat
            })
    print(len(pasta))
    #all_product.append(pasta)
    #############################################################################################################
    inputElement = driver.find_element_by_xpath('//*[@id="navbar"]/ul/li[3]/a').click()
    items  = [i.text for i in driver.find_elements_by_class_name("left-con-pizzas")]
    price  = [i.text for i in driver.find_elements_by_class_name("pro_price")]
    price = ' '.join(price).split()
    #price= [re.sub('[^\d\.]', '', price[i]) for i in range(len(price))]
    desc = [i.text for i in driver.find_elements_by_class_name("short_desc")]
    cat = [i.text for i in driver.find_elements_by_xpath('//*[@id="navbar"]/ul/li[3]/a')]
    cat = cat[0]
    for  i in range(len(items)):
            appatizers.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": cat
            })
            all_product.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": cat
            })        
    print(len(appatizers))
    #all_product.append(appatizers)
    #######################################################################
    inputElement = driver.find_element_by_xpath('//*[@id="navbar"]/ul/li[5]/a').click()
    items  = [i.text for i in driver.find_elements_by_class_name("left-con-pizzas")]
    price  = [i.text for i in driver.find_elements_by_class_name("pro_price")]
    #price= [re.sub('[^\d\.]', '', price[i]) for i in range(len(price))]
    price = ' '.join(price).split()
    desc = [i.text for i in driver.find_elements_by_class_name("short_desc")]
    cat = [i.text for i in driver.find_elements_by_xpath('//*[@id="navbar"]/ul/li[5]/a')]
    cat = cat[0]
    for  i in range(len(items)):
            drinks.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": cat
            })
            all_product.append({
            "item_name": items[i],
            "description": desc[i],
            "price": int(price[i]),
            "catagory": cat
            })
    print(len(drinks))
    
    #######################################################################
    #all_product.append(drinks)//*[@id="navbar"]/ul/li[4]/a
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
        cat = [i.text for i in driver.find_elements_by_xpath('//*[@id="navbar"]/ul/li[4]/a')]
        cat = cat[0]
        deals.append({
            "item_name": items.text,
            "description": desc.text,
            "price": int(price),
            "catagory": cat
            })
        all_product.append({
            "item_name": items.text,
            "description": desc.text,
            "price": int(price),
            "catagory": cat
            })
    print(len(deals))
    #####################################################################
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
    print(len(all_product))
    #print(all_loaction)
    driver.quit()
    
    import pyrebase 
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
    
    db.child("Database").child("pizzahut").child("Menu").set(all_product)
    db.child("Database").child("pizzahut").child("Locations").set(all_loaction)
#scrap_upload_pizzahut()