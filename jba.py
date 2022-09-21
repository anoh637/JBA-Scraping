import requests
from bs4 import BeautifulSoup


headers = {"User-Agent": 
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}

def get_url():
    for count in range (1,7):
        url = f"https://www.jba.co.id/en/lelang-motor-kota/lelang-motor/detail/2629?page={count}&direction=ASC"

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml") #html.parser

        data = soup.find_all("div", class_="col-lg-4 col-sm-6")

        for i in data:
            card_url = "https://www.jba.co.id/" + i.find("a").get("href")
            yield card_url

def array():
    for card_url in get_url():
            response = requests.get(card_url, headers=headers)
            soup = BeautifulSoup(response.text, "lxml")

            data = soup.find("div", class_="content-wrapper page-detailvehicle")
            
            year = data.find("div", class_="vehicle-year dottedline").text.replace("Year : ", "").strip()
            date = data.find("div", class_="bidding-date dottedline").text.replace("Auction : ", "").strip()
            location = data.find("div", class_="bidding-place dottedline").text.strip()
            price = data.find("div", class_="limit-price").text.replace("Price Limit", "").strip()
            engine_grade = data.find("div", class_="").text.replace("Engine","").strip()
            exterior_grade = data.find("div", class_="").find_next("div", class_="").text.replace("Eksterior","").strip()
            container = data.find("div", class_="detail-info detail-car-info")
            
            container_1 = data.find("div", class_="detail-info-group")
            brand = container_1.find("div", class_="item-content").text.strip()
            model = container_1.find("div", class_="item-content").find_next("div", class_="item-content").text.strip()
            engine_capacity = container_1.find("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").text.strip()
            fuel = container_1.find("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").text.strip()
            odometer = container_1.find("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").text.strip()
            outline_number = container_1.find("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").text.strip()
            engine_number = container_1.find("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").text.strip()
            
            container_2 = data.find("div", class_="detail-info-group").find_next("div", class_="detail-info-group")
            police_number = container_2.find("div", class_="item-content").text.strip()
            colour = container_2.find("div", class_="item-content").find_next("div", class_="item-content").text.strip()
            stnk = container_2.find("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").text.strip()
            validity_stnk = container_2.find("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").text.strip()
            bpkb = container_2.find("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").text.strip()
            faktur = container_2.find("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").text.strip()
            fotokopi_ktp = container_2.find("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").text.strip()
            kwitansi_blanko = container_2.find("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").text.strip()
            form_a = container_2.find("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").find_next("div", class_="item-content").text.strip()
            yield date, location, price, engine_grade, exterior_grade, brand, model, year, engine_capacity, fuel, odometer, outline_number, engine_number, police_number, colour, stnk, validity_stnk, bpkb, faktur, fotokopi_ktp, kwitansi_blanko, form_a
 