# 1. Tangerang Kota

# 1.1.Import all the libraries needed
# Before importing the libraries; on your terminal environment, install all the module: pip install requests, beautifulsoup4, lxml
from bs4 import BeautifulSoup # Beautiful Soup is to process the raw data and make it beautiful
from time import sleep # Sleep is used to limit the processing time
import requests # Request all the module


# 1.2. Choose Headers
# Headers are optional but needed to avoid getting blacklisted by the website, you can put any headers such as Chrome, here I use Mozilla
headers = {"User-Agent": 
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}

# 1.3. Connect to Website 
def get_url(): # Looping Function
    for count in range(1, 400): # Choose page length

        url = "https://www.olx.co.id/tangerang-kota_g4000079/motor-bekas_c200" # Choose the page url's of your choosing

        response = requests.get(url, headers=headers) # Here we request the url 

        soup = BeautifulSoup(response.text, "lxml") #html.parser

        # Find Products in the url
        data = soup.find_all("li", class_="EIR5N") # Here we put the class of each products, OLX has this class for their product list

        for i in data:
            card_url = "https://www.olx.co.id/" + i.find("a").get("href") # Here we click each of the products in the product list
            yield card_url

# 1.4. Connect to each url and get the data
def array(): # Looping function
    for card_url in get_url(): # Looping function
        response = requests.get(card_url, headers=headers) # Here we requests to the product url
        sleep(10) # You can put any seconds in the sleep function, for trial use 1 seconds, for access the data use 20 seconds, depend on how fast your internet connection
        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find("main", class_="_1_dLE _20mSp") # Here is the pool data of the product, all details are listed in this class
        
        # We use try and except to avoid attribute error if some product does not have all the data we requested
        try:
            brand = data.find("span", class_="_2vNpt").text.strip()
        except:
            brand = 'none'
        try:
            model = data.find("span", class_="_2vNpt").find_next("span", class_="_2vNpt").text.strip()
        except:
            model = 'none'
        try:
            mileage = data.find("span", class_="_2vNpt").find_next("span", class_="_2vNpt").find_next("span", class_="_2vNpt").find_next("span", class_="_2vNpt").text.strip()
        except:
            mileage = 'none'
        try:
            seller_type = data.find("span", class_="_2vNpt").find_next("span", class_="_2vNpt").find_next("span", class_="_2vNpt").find_next("span", class_="_2vNpt").find_next("span", class_="_2vNpt").text.strip()
        except:
            seller_type = 'none'
        try:
            price = data.find("span", class_="_2xKfz").text.strip()
        except:
            price = 'none'
        try:
            year = data.find("span", class_="_18gRm").text.strip()
        except:
            year = 'none'
        try:
            area = data.find("span", class_="_2FRXm").text.strip()
        except:
            area = 'none'
        try:
            post_title = data.find("h1", class_="_3rJ6e").text.strip()
        except:
            post_title = 'none'
        try:
            post_date = data.find("div", class_="_2DGqt").text.strip()
        except:
            post_date = 'none'
        try:
            post_description = data.find("p").text.strip()
        except:
            post_description = 'none'
        yield brand, model, mileage, seller_type, price, year, area, post_title, post_date, post_description, card_url # Output       
        
 