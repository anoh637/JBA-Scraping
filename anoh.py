# This is OLX code for mass scrapper, please see explanation of each code on run.py
# To run this code, you need to access the website inspector -> click Network -> click XHR -> click 'load more' on the web page -> and analyze the API that load the page
# After getting the fixed API for loading more content -> install insomnia (or others of your choosing) -> paste the link -> broad the facet_limit (for olx unique case) -> broad the location_facet_limit -> generate the code -> choose Python -> choose Requests -> Copy/Paste to your Code editor
import requests
from bs4 import BeautifulSoup

url = "https://www.olx.co.id/api/relevance/v2/search"
 
for X in range (1,3):
    querystring = {"category":"200","facet_limit":"2500","location":"2000007","location_facet_limit":"2500","make":"motor-bekas-honda,motor-bekas-kawasaki,motor-bekas-yamaha,motor-bekas-suzuki","nested-filters":"{\"make\":[{\"motor-bekas-honda\":{}},{\"motor-bekas-kawasaki\":{}},{\"motor-bekas-yamaha\":{}},{\"motor-bekas-suzuki\":{}}]}","page":f"{X}","platform":"web-desktop","user":"183452dfa09x70449f75"}
    headers = {
        "cookie": "laquesis=pan-59312%40a%23pan-59740%40a%23pan-60601%40b%23pan-67471%40b; lqstatus=1663331308; _abck=89DC7B3E52DFCCEA41FE59338C95BF48~-1~YAAQVSg0FwbtZFaDAQAAgJHWWgjLyNeH5NIjNbKW8JbUmL1NMHdZmsABxrSAWlQ8oUprKkK0U7Gt17TB26IXfhVjai%2B7Rt3Z%2Bzwcjdbhsx2zMU63ruIZ5j7ud7i3AiztT2fanhmxzX9UR8SnOy4C75APlG185qYtGNC6Bg8SfIHxq4ESCuWvQB05TURbY1%2BIJ1G46b8zQA5nEqmb6rqwu2tWfwyRAlHw3d%2F3SZNykK8PI0v6Cdx0d%2Bf1fk7759i4R%2B6eF2xyjXHV0GZEB7rkxINbNC9V%2FciPAm9Vy7XLKr5XnNCHdDTG1yL3bzl3TS2FJ%2F%2F0FB6Z6ClGk%2FxcfQb%2BS7UVK%2BacvP6uZVci1EAWtuLSPtYFftTVFzI5e8qnA5%2FFMMmICZUi~-1~-1~-1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "X-NewRelic-ID": "VQMGU1ZVDxABU1lbBgMDUlI=",
        "x-panamera-fingerprint": "0a08e75dcc0f707eb29265032e0af3a5#1663312986081",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        "Referer": "https://www.olx.co.id/jakarta-dki_g2000007/motor-bekas_c200?filter=make_eq_motor-bekas-honda_and_motor-bekas-kawasaki_and_motor-bekas-yamaha_and_motor-bekas-suzuki",
        "Connection": "keep-alive",
        "Cookie": "laquesis=pan-59312@a#pan-59740@a#pan-60601@b#pan-67471@b; lqstatus=1663681778||||; _abck=520CC4EAC23A808D1FB14546E11E08E0~-1~YAAQFWswF9Nh/DiDAQAA1m8mWwgzLtM+6MV/PUPE3lCUmUMMAV3WI2z5IfPl/UXMcr+FKyHm5OmZNpjIesVwpUEUDLgwI+Vx8qc9LtrvtjtZR5eG1uOtn5GTQ3Ko7KdfVYvtWrYQLtDTxYIl0X13hPtIEAyStqVO6lyvE80iKeA+QaCwuqWLwblRlsJC0Coo+aFUkvSjtk/lIGDPj396dw3AIp8T6S104IJo/dW3yIaUdjR9V9MvK/h01qJhVWftwy0tigoi22rxF2BUUxRhy13TZ6mKHLzeDoljcE//uXGWlXJsbgkhwq0I1wcvmQLQ0eTJgOR/XAEq1Yc+EYRdDi2dY8GBdOByWHTCnNKgz4ZWqgBdtv0tBboLbnMx207pRwWRGzaRbfke5A==~-1~-1~-1; onap=183452dfa09x70449f75-7-1835b262727x23511a5b-5-1663683371; __exponea_etc__=308b7106-f4b7-49d7-b0f5-b5928dd156e7; WZRK_G=ab74907d79574521aa1f9a6bf381fe88; laquesisff=; laquesissu=; locationPath=%5B%7B%22id%22%3A2000007%2C%22name%22%3A%22Jakarta%20D.K.I.%22%2C%22type%22%3A%22STATE%22%2C%22longitude%22%3A106.84513%2C%22latitude%22%3A-6.21462%2C%22parentId%22%3A1000001%7D%5D; ak_bmsc=777531AAEA1C32D959BCD5FAB5EF15A8~000000000000000000000000000000~YAAQTig0F8cc6EKDAQAAr70DWxFjLyyGnA19oGkhLIZGUBCaY6hY5v0tgGxZSfUS7iT0rOXKO17NpHoJPUVadxaUaRzQD1w464FHaR9taDRRHNfqdrUKLiKze4SPQyoAkbUhldKEdRfjRrkofo1XB2lp/WH0gUJLU6xLsSzP8gW7BC5GWjEFj37zrMAGzupWvpbQHUzzf5S4tksvhYUcLcdTOhwEmrkzoWdf/xlhXRR0futd+xZBlfifi6DBrpzD8oOfW8LnshzHsh6PRtBlvIvE/FA0jRKcpA6+8ovLVxGSsLSxCERmb8UqWcQTfm73hHoVksJsP9bx9/D+e6cYrKPd+il8ZRDvqEFpNmGq4wqCjq/t1sCY7UIi+4YRS5qvgb8pVdkU41wd6fHtpsCdrQIxQbpzV6DG5Zo2fnHJtuq1MrP7LnCxLfBSUM+zFQq+OPDN5qP2YUfkdQhXEoQ4Tl3Q3uBlvr/mzLxSf5RZssDqMkrV6Z3C+s4F; bm_sz=38D1EC32D6A0DCA1DD16B4418DA747BF~YAAQTig0FyEZ6EKDAQAA86ADWxHavs5jX3DRttCb0H7rEwgoprbY03lDFd7RCXuVFxRdLzIDw/gl6yHMGDm3IQHth7FsfIgKoembRsnC0WLU8uiN37xaYJlRJuisBLXnzx722sohyDvWgDABNM85+RWZJ7Z0RRhILGMxK2eiWqAasKSFT9f4uF61VYBvpaeTY4/eVhdJiKmACPyk4sf6gXZ4nW7kH5bRQWimfkauQdf3lQ8ZI56f4tXLzjRGQsXk5EoOPbbfu+xTfzPYnxl4lEbyto2D8/L1nNhavdWWV19Qdg==~3422017~4538949; bm_sv=85E1C77DB9A7DABF33F31C31A71D6723~YAAQDmswF1rHQ1aDAQAAyComWxFsa2RFSSTW1yfxAXA6iazt56ZL16JEVGkyrBPtvEfrEJ/tQABiunlvMPn7MG/lzTZhPth3c+w3rKZPE3uyCHn4rucM9/R7yigtLxsb0VUadkRsygIISDjmazfl29W53B7nne6JiJgi7/oyClopCqFrGvfSYczGcvpyDhdPI6+VQHxFXxYfOkQ12Yiglja0iolDS90OiI72cRCi9NGWVkIPMJkHHtJrHvQ4poCK~1; __exponea_time2__=0.48490476608276367; ldTd=true; WZRK_S_W6K-746-995Z=%7B%22p%22%3A1%2C%22s%22%3A1663681571%2C%22t%22%3A1663681571%7D",
        "TE": "trailers"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
        
    soup = BeautifulSoup(response.text, "lxml") #html.parser

    data = soup.find_all("li", class_="EIR5N")
    for i in data:
        card_url = "https://www.olx.co.id/" + i.find("a").get("href")
             

def array():
    for card_url in range():
        response = requests.request("GET", url)
        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find("main", class_="_1_dLE _20mSp")
                
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
        yield brand, model, mileage, seller_type, price, year, area, post_title, post_date, post_description, card_url
