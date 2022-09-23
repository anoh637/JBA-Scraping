# This is OLX code for mass scrapper, please see explanation of each code on run.py
# To run this code, you need to access the website inspector -> click Network -> click XHR -> click 'load more' on the web page -> and analyze the API that load the page
# After getting the fixed API for loading more content -> install insomnia (or others of your choosing) -> paste the link -> broad the facet_limit (for olx unique case) -> broad the location_facet_limit -> generate the code -> choose Python -> choose Requests -> Copy/Paste
import requests
from bs4 import BeautifulSoup

url = "https://www.olx.co.id/api/relevance/v2/search"

def get_url(): 
    for X in range (1,2):
        querystring = {"category":"200","facet_limit":"100","location":"2000007","location_facet_limit":"20","make":"motor-bekas-yamaha","nested-filters":"{\"make\":[{\"motor-bekas-yamaha\":{}}]}","page":f"{X}","platform":"web-desktop","user":"183452dfa09x70449f75"}
        headers = {
        "cookie": "laquesis=pan-59312%40a%23pan-59740%40a%23pan-60601%40b%23pan-67471%40b; lqstatus=1663331308; _abck=89DC7B3E52DFCCEA41FE59338C95BF48~-1~YAAQr9t5LTXof1iDAQAAxZIPaQhuj%2BrQlHljG3FiCoYT6ILqG0pIkV5u%2FlQqnuqLZ%2F8KUwJDCMlkWF462aZ1yPwRmFP5jbVw6TMVs%2Bi0OES3K6Z1kk0YDa1x1J8g180ivCmpjK4DpezeKdsLAOqn38JxIM8a6rmlruARx692YtZKcIemfmGR%2FUoHdB8yZ%2B238QqEoD%2Faf8rc4nrsVDSZpc0WcrtK9BQkYoyQiZ5JTh7TeHu%2F5dWnlHvM71Z7c1EuRm2PZvj0xMf3z7cKKPACd2LJRzKAOfXuW5PCPc2Sf0M0b3OFKtMlmE%2Fql7hWrsysFckD45dwksETp6ia1BHzMNejLYRsTU4jIis6Ng%3D%3D~-1~-1~-1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "x-panamera-fingerprint": "0a08e75dcc0f707eb29265032e0af3a5#1663312986081",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        "Referer": "https://www.olx.co.id/jakarta-dki_g2000007/motor-bekas_c200?filter=make_eq_motor-bekas-yamaha",
        "Connection": "keep-alive",
        "Cookie": "laquesis=pan-60601@b#pan-67471@b; lqstatus=1663916068|18367e66510x7b8dd592|pan-60601||; _abck=520CC4EAC23A808D1FB14546E11E08E0~-1~YAAQt9t5Lf/kCUSDAQAAg10OaQgaGqlqjNZDTZBZw8f/m72MyVjxe+PA/00dFWdFO7q7HZmGDH+Nlg/U/oGhLgCkzn6/G8J1ekeFg5zzcEORL2ILzu0defMb+R03+ROBnoB0vfUzKb0uLyCiLNrbdVrltyI+8C6QdgCMRGRqgbCsLknn7LIOjT/mNuS1Vm6rQIipDqD2qRXMI8InMvM4yeSGzTPsPWiSzR7uXSGCbLBK0HCyv7auzYA9Cyt4au20Q1Fh/RIfyG1i6vaLYAj2ZVCjKRkVuz94wyUB+wDztMXG6uPCsyYgj2JgABMcB+YlH3D/EWPIGg9hF62kb+Dtbtqh/GHCs3avEtpuX2ROAB8=~-1~-1~-1; onap=183452dfa09x70449f75-13-18369012152x6800c191-10-1663916144; __exponea_etc__=308b7106-f4b7-49d7-b0f5-b5928dd156e7; WZRK_G=ab74907d79574521aa1f9a6bf381fe88; laquesisff=; laquesissu=; bm_sz=1C8B50C22887FB2A599AF545E41E13D4~YAAQ9tt5LbnQCGSDAQAAaZRbaBFJ3LzNePdigQoZ788XZf56X2gMzrhpkPwZ1+laa4YtNFxmKA6Kj2yEb6pj2O3iX0vSFvUmWPYHWLd0emIGXEtL24j9EAtUtsnMZYUvu4tRlApBdFIOUBze1eQTWDP4njosGvM7HaFS13+I3gSPhbt6xg3TSXOrC5MT2GyEFR+Qm+h1jtRksHfkEFBqZEBr1Twp6r7Y4jfTUElUkgdqWNaRPqZeKZg1R6Db/XFxfD9+zfhkJordsPRB4FA7PlGpEWwEZ9VNHxpHEKFzpC6zu++iyTAK16V40Ta3Win2x9Ao7EwvxGRNbw==~3486785~3749430; locationPath=%5B%7B%22id%22%3A4000080%2C%22name%22%3A%22Tangerang%20Selatan%20Kota%22%2C%22type%22%3A%22CITY%22%2C%22longitude%22%3A106.71346%2C%22latitude%22%3A-6.28731%2C%22parentId%22%3A2000004%7D%5D; ldTd=true; bm_sv=BCCBBDEFB48C0DC052DB41A32C31D97D~YAAQt9t5LQDlCUSDAQAAg10OaRGIH8PohGqpNUzXYhLZPSVU81o5CMkHBrmYfYbxT4f8bsggU5/BlCsPqaEMxniGLbbvP9M83cJWwaUuFlvUdt8CyNkPrpCloc0PtvX9B0yfOUVZv+ngZfUIux19JRZu8MMV8vXJCxZwzpZqyEdlxQxLg4v70T5K2M7Eyc+vhQ+le36HTTPA4+Ulcj8KC1mdGy56PTOCI9vXiftej5/9qqIL8QuAFfAUsKjM0QlT~1; ak_bmsc=AC634AAF18FB93D7517E474FAD551B33~000000000000000000000000000000~YAAQrtt5LZFp3leDAQAA3iABaRGmt/xsJevfz3TU/tre3EEWzA+4XVtM2wexBaeOLQAiHT/Fp9fia63xhnGbybzt0to640Ck2s9gNydP6Fp3cQashmCqmoDgvQ3wWD3Fwf/LS1DVM9GknhBILLJoN6mi1bEVJvvB+DqjK+O6r5GXGkaT50UJOmWkxmRfsHiSVNf4/K8g6a/u1Rd6I8QCGFyg/DCTgM/CO2EMrrlC28K6bdTP/FeK9ZU8/frRmZjqCet+ggOOl9WDg+SXEVs8hK3T2hmTTKI2/s2dVuP3w01lYG0E/5SbVHO/ZH/AoIKXAIuOGj/87et1Q1vIPUy5E1wfWSBXk64RxvCtGkvoR91O52WeTFrWBiPAAP4OTnh7tSVQ4KBe6MnhZLfOYhUHcv+xoKy20XxZACB88geFseK4V6M+/1a+LeJI9e2KGnG91BnfIdu73Kf97Ur6Es9auHTD; bm_mi=56C258222BB09074A1818DB067D6167F~YAAQrtt5LVdp3leDAQAAoxYBaRGvUibMCXqQBnG662YQHUf5oE/c1DIG2MewE/tT0QN52jHYBhw4KEQWHLg8HsW+/WTGOsr7XavmQO8bq3hOSTvxAZTa/+ZtNTn+eeD6IgYD4EzmBV1ba5voM0z8Mr2Sawz0R9d/y0CN2hfz0TNfa7JanIdX+RcwUogchJseOJMuJWg2cPVCTHS9ZDaN4u7nssJAxzAmcgKsvvLzOfh9IN1BB7sPjiEqaOZcsfRjjS3KJvowIXmdtpluPVuye3wmeEItS9LQuhynNEAVuSDxqNKAvQ4HPUJ4roTbBav98g/e+ILoTWNhnCqFORRJn5CeAI39Uxl8+7zcAmbcVPzMG86V~1; WZRK_S_W6K-746-995Z=%7B%22p%22%3A2%2C%22s%22%3A1663914026%2C%22t%22%3A1663914465%7D",
        "TE": "trailers"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)           
        soup = BeautifulSoup(response.text, "lxml") #html.parser
        data = soup.find_all("li", class_="EIR5N")
        for i in data:
            card_url = "https://www.olx.co.id/" + i.find("a").get("href")
            yield card_url
             

def array():
    for card_url in get_url():
        response = requests.get(card_url)
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
