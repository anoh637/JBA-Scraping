import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent": 
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}

def get_url():
    url = "https://www.olx.co.id/jakarta-dki_g2000007/motor-bekas_c200?filter=make_eq_motor-bekas-honda_and_motor-bekas-kawasaki_and_motor-bekas-yamaha_and_motor-bekas-suzuki"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml") #html.parser

    data = soup.find_all("li", class_="EIR5N")

    for i in data:
        card_url = "https://www.olx.co.id/" + i.find("a").get("href")
        yield card_url

def array():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find("main", class_="_1_dLE _20mSp")
        
        details = data.find("div", class_="_3JPEe").text
        brand = data.find("span", class_="_2vNpt").text
        model = data.find("span", class_="_2vNpt").find_next("span", class_="_2vNpt").text
        mileage = data.find("span", class_="_2vNpt").find_next("span", class_="_2vNpt").find_next("span", class_="_2vNpt").find_next("span", class_="_2vNpt").text
        seller_type = data.find("span", class_="_2vNpt").find_next("span", class_="_2vNpt").find_next("span", class_="_2vNpt").find_next("span", class_="_2vNpt").find_next("span", class_="_2vNpt").text
        price = data.find("span", class_="_2xKfz").text
        year = data.find("span", class_="_18gRm").text
        area = data.find("span", class_="_2FRXm").text
        post_title = data.find("h1", class_="_3rJ6e").text
        post_date = data.find("div", class_="_2DGqt").text
        post_description = data.find("p").text
        yield details, price, year, area, post_title, post_date, post_description
    
    