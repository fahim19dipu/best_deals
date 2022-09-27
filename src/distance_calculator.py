from selenium import webdriver 
import time
from selenium.webdriver.chrome.options import Options
import re
################################### calculate and return user location againt all locations of a resturant.
def calc_distance(location, destination):
    chrome_options = Options()
    #chrome_options.add_argument("USER AGENT")
    chrome_options.add_argument("--disable-extensions")
    #chrome_options.add_argument("--disable-gpu")
    #chrome_options.add_argument("--no-sandbox") # linux only
    #chrome_options.add_argument("--headless")
    # prefs = {"profile.managed_default_content_settings.images": 2}
    # chrome_options.add_experimental_option("prefs", prefs)
    #chrome_options.headless = True # also works
    
    driver = webdriver.Chrome('C:/Users/user/Desktop/chromedriver_win32/chromedriver',options=chrome_options)

    #driver = webdriver.Chrome('C:/Users/user/Desktop/chromedriver_win32/chromedriver')
    driver.minimize_window()
    url = 'https://www.mapsofworld.com/bangladesh/distance-calculator/'
    driver.get(url)
    #print(driver.title)
    distance_list =[]
    inputElement = driver.find_element_by_xpath('//*[@id="start"]')
    inputElement.click()
    inputElement.send_keys(location)
    for i in range(len(destination)):
        inputElement = driver.find_element_by_xpath('//*[@id="end"]').clear()
        inputElement = driver.find_element_by_xpath('//*[@id="end"]')
        inputElement.click()
        inputElement.send_keys(destination[i])
        inputElement = driver.find_element_by_xpath('//*[@id="getRoute"]')
        inputElement.click()
        time.sleep(6)
        outputElement = driver.find_element_by_xpath('//*[@id="sidepanel"]/div/div/div[3]/div[1]/span[1]')
        val = outputElement.text
        distance= re.sub('[^\d\.]', '', val) ## remove all non digit elements
        #distance = val.replace(" km","") ##
        print(distance)
        distance_list.append(float(distance))
    driver.quit()
    return distance_list
# location = "jigatola"
# destination = ["24/A, Tipu Sultan Road, Valencia Building (near Wari Thana), Wari 1203, Dhaka Division, Dhaka.",
#                 "Plot- 50, Road- 11, Block- C, Banani Police Station, Banani, Dhaka-1213."]
# distances = calc_distance(location, destination)

