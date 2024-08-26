from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import urllib.parse
import json


def get_tesla_inventory(query):
    encoded_query = urllib.parse.urlencode({"query": json.dumps(query)})
    url = 'https://www.tesla.com/inventory/api/v4/inventory-results?' + encoded_query
    try:
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        #chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        #Change in Selenium 4.10.0, this no longer works
        chrome_service = Service(executable_path=r'C:\\Dev\\tesla_inventory_scraper\\chromedriver-win64\\chromedriver.exe')
        browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
        browser.get(url)
    except TimeoutException:
        print('Loading took too much time!')
    else:
        html = browser.page_source
    finally:
        browser.quit()
        return html


queries = {
    "Used Model 3": {
        "query": {
            "model": "m3",
            "condition": "used",
            "options": {},
            "arrangeby": "Price",
            "order": "asc",
            "market": "CA",
            "language": "en",
            "super_region": "north america",
            "lng": -73.8625405,
            "lat": 45.6450559,
            "zip": "H2L5E4",
            "range": 0,
            "region": "QC",
        },
        "offset":0,
        "count":500,
        "outsideOffset":0,
        "outsideSearch": False,
        "isFalconDeliverySelectionEnabled": False,
        "version": None
    }
}



for query in queries: 
    print(datetime.now().strftime("%H:%M:%S") + " Searching Tesla's website for: " + query)
    tmp_inv_data = get_tesla_inventory(queries[query])
    soup = BeautifulSoup(tmp_inv_data, 'html.parser')
    #print(soup.prettify())
    pre = soup.find('pre').string
    #print(pre)
    cars_json = json.loads(pre)
    
    for car in cars_json["results"]:
        print(car["Year"]," ",car["Model"],"(",car["TotalPrice"],"$ )")
        print("\t","Trim: ",car["TrimName"],"(",car["TRIM"][0],")")
        print("\t","Color: ",car["PAINT"][0])
        print("\t",car["OdometerType"],":",car["Odometer"])
        print("\t","Vin: ",car["VIN"])
        print("\t","IsDemo: ",car["IsDemo"])
