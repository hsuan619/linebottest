from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests
import urllib.request
import json
import time
import googlemaps



# 美食抽象類別
class Food(ABC):
     
    def __init__(self, area, category, price):
        self.area = area  # 地區
        self.category = category
        self.price = price
    @abstractmethod
    def scrape(self):
        pass
 
 
# 愛食記爬蟲
class IFoodie(Food):
 
    def scrape(self):
        response = requests.get(
            "https://ifoodie.tw/explore/" + self.area +
            "/list/" + self.category +
            "?priceLevel=" + self.price +
            "&sortby=popular&opening=true")
        
        soup = BeautifulSoup(response.content, "html.parser")

        cards = soup.find_all(
            'div', {'class': 'jsx-558691085 restaurant-info'}, limit=6)
 
        content = ""
        for card in cards:
 
            title = card.find(  # 餐廳名稱
                "a", {"class": "jsx-558691085 title-text"}). getText()

            stars = card.find(  # 餐廳評價
                "div", {"class": "jsx-1207467136 text"}).getText()
            address = card.find(  # 餐廳地址
                "div", {"class": "jsx-558691085 address-row"}).getText()

            opening = card.find(
                "div",{"class": "jsx-558691085 info"}).getText()
            
            url = card.find(
                "a",{"class":"jsx-558691085"}).get("href")
            #將取得的餐廳名稱、評價及地址連結一起，並且指派給content變數
            content += f"{title}  ⭐{stars}顆星\n\n🚗  {address}\n⏱  {opening}\n\n更多資訊：https://ifoodie.tw{url}\n\n"
 
        return content




cities= ["臺北市","新北市","桃園市","臺中市","臺南市","高雄市","基隆市","新竹市","嘉義市","新竹縣",
        "苗栗縣","彰化縣","南投縣","雲林縣","嘉義縣","屏東縣","宜蘭縣","花蓮縣",]
gmaps = googlemaps.Client(key='AIzaSyBNJF0jfTo28cI4eFHXjn5DmbxVr8d9paM')
ids = []
for city in cities:
    results = []
    # Geocoding an address
    geocode_result = gmaps.geocode(city)
    loc = geocode_result[0]['geometry']['location']
    query_result = gmaps.places_nearby(keyword="餐廳",location=loc, radius=500)
    results.extend(query_result['results'])
    while query_result.get('next_page_token'):
        time.sleep(2)
        query_result = gmaps.places_nearby(page_token=query_result['next_page_token'])
        results.extend(query_result['results'])    
    for place in results:
        ids.append(place['place_id'])

stores_info = []
# 去除重複id
ids = list(set(ids)) 
for id in ids:
    stores_info.append(gmaps.place(place_id=id, language='zh-TW')['result'])

print(ids)