from abc import ABC, abstractmethod

from linebot.models import *

# 訊息抽象類別
class Message(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def content(self):
        pass

# 「選擇地區」按鈕樣板訊息

# 「選擇美食類別」按鈕樣板訊息
class AreaMessage(Message):
     def content(self):
        Carousel_templateArea = TemplateSendMessage(
        alt_text='Carousel template',  #只能塞三個action 每個column數量要一致 最多5個carousel
        template=CarouselTemplate(
        columns=[
                CarouselColumn(
                thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/6/67/%E9%9B%B2%E5%98%89%E5%8D%97.png',
                title='雲嘉南',
                text='選擇地區',
                actions=[
                                PostbackTemplateAction(
                                label='雲林縣',
                                text='雲林縣',
                                data='A&雲林縣'
                                ),
                                PostbackTemplateAction(
                                label='嘉義市',
                                text='嘉義市',
                                data='A&嘉義市'
                                ),
                                PostbackTemplateAction(
                                label='臺南市',
                                text='臺南市',
                                data='A&臺南市'
                                )
                                
                            ]   
                        ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/%E5%8C%97%E5%8C%97%E5%9F%BA%E5%AE%9C.png/749px-%E5%8C%97%E5%8C%97%E5%9F%BA%E5%AE%9C.png',
                    title='北北基',
                    text='選擇地區',
                    actions=[
                                PostbackTemplateAction(
                                label='台北市',
                                text='台北市',
                                data='A&台北市'
                                ),
                                PostbackTemplateAction(
                                label='新北市',
                                text='新北市',
                                data='A&新北市'
                                ),
                                PostbackTemplateAction(
                                label='基隆市',
                                text='基隆市',
                                data='A&基隆市'
                                )
                            ]
                        ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/%E4%B8%AD%E5%BD%B0%E6%8A%95.png/749px-%E4%B8%AD%E5%BD%B0%E6%8A%95.png',
                    title='中彰投',
                    text='選擇地區',
                    actions=[
                                    PostbackTemplateAction(
                                    label='台中市',
                                    text='台中市',
                                    data ='A&台中市'
                                    ),
                                    PostbackTemplateAction(
                                    label='彰化縣',
                                    text='彰化縣',
                                    data='A&彰化縣'
                                    ),
                                    PostbackTemplateAction(
                                    label='南投縣',
                                    text='南投縣',
                                    data='A&南投縣'
                                )
                            ]
                        ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/%E6%A1%83%E7%AB%B9%E8%8B%97.png/749px-%E6%A1%83%E7%AB%B9%E8%8B%97.png',
                    title='桃竹苗',
                    text='選擇地區',
                    actions=[
                                    PostbackTemplateAction(
                                    label='桃園市',
                                    text='桃園市',
                                    data='A&桃園市'
                                    ),
                                    PostbackTemplateAction(
                                    label='新竹市',
                                    text='新竹市',
                                    data='A&新竹市'
                                    ),
                                    PostbackTemplateAction(
                                    label='苗栗縣',
                                    ext='苗栗縣',
                                    data='A&苗栗縣'
                                    )
                                ] 
                            ),
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/1/1a/%E9%AB%98%E5%B1%8F%E6%BE%8E.png',
                        title='高屏澎(?)',
                        text='選擇地區',
                        actions=[
                                        PostbackTemplateAction(
                                        label='高雄市',
                                        text='高雄市',
                                        data='A&高雄市'
                                        ),
                                        PostbackTemplateAction(
                                        label='屏東縣',
                                        text='屏東縣',
                                        data='A&屏東縣'
                                        ),
                                        PostbackTemplateAction(
                                        label='澎湖縣',
                                        text='澎湖縣',
                                        data='A&澎湖縣'
                                        )
                                    ]
                                ),
                        CarouselColumn(
                            thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/%E8%8A%B1%E6%9D%B1.png/749px-%E8%8A%B1%E6%9D%B1.png',
                            title='宜花東',
                            text='選擇地區',
                            actions=[
                                            PostbackTemplateAction(
                                            label='宜蘭縣',
                                            text='宜蘭縣',
                                            data='A&宜蘭縣'
                                            ),
                                            PostbackTemplateAction(
                                            label='花蓮縣',
                                            text='花蓮縣',
                                            data='A&花蓮縣'
                                            ),
                                            PostbackTemplateAction(
                                            label='臺東縣',
                                            text='臺東縣',
                                            data='A&臺東縣'
                                            )
                                        ]
                                    )
                                ]
                            )
                        )
        return Carousel_templateArea
class Category2Message(Message):  # 如果回傳值為「選擇地區」回復「選擇美食類別」按鈕樣板訊息
    def __init__(self, kind):
        self.kind = kind 
    def content(self):
        Carousel_templatecate = TemplateSendMessage(
                        alt_text='Carousel template',  #只能塞三個action 每個column數量要一致 最多5個carousel
                        template=CarouselTemplate(
                        columns=[
                                CarouselColumn(
                                    thumbnail_image_url='https://www.welcometw.com/wp-content/uploads/2020/11/%E8%80%81%E9%BC%8E%E6%97%BA-1-825x510.jpg',
                                    title='今天想吃什麼呢?',
                                    text='請選擇美食類別',
                                    actions=[
                                            PostbackTemplateAction(
                                            label='火鍋',
                                            text='火鍋',
                                            data='D&火鍋'
                                            ),
                                            PostbackTemplateAction(
                                            label='燒烤',
                                            text='燒烤',
                                            data='D&燒烤'
                                            ),
                                            PostbackTemplateAction(
                                            label='吃到飽',
                                            text='吃到飽',
                                            data='D&吃到飽'
                                            )
                                        ]
                                    ),
                                    CarouselColumn(
                                    thumbnail_image_url='https://doqvf81n9htmm.cloudfront.net/data/jamiesu_149/2020SEP/0904/DF4.jpg',
                                    title='今天想吃什麼呢?',
                                    text='請選擇美食類別',
                                    actions=[
                                            PostbackTemplateAction(
                                            label='日式料理',
                                            text='日式料理',
                                            data='D&日式料理'
                                            ),
                                            PostbackTemplateAction(
                                            label='韓式料理',
                                            text='韓式料理',
                                            data='D&韓式料理'
                                            ),
                                            PostbackTemplateAction(
                                            label='拉麵',
                                            text='拉麵',
                                            data='D&拉麵'
                                            )
                                        ]
                                    ),
                                    CarouselColumn(
                                    thumbnail_image_url='https://wowlavie-aws.hmgcdn.com/file/article_all/%E4%B8%80%E6%A8%93%E8%A5%BF%E5%BC%8F%E6%8B%B1%E5%BD%A2%E9%85%92%E6%9E%B6%E6%93%BA%E7%BD%AE%E4%BA%86%E8%A8%B1%E5%A4%9A%E5%BA%97%E5%85%A7%E9%85%92%E6%AC%BE%E3%80%81%E5%85%AC%E4%BB%94%E6%94%B6%E8%97%8F%EF%BC%88%E5%81%B4%E9%82%8A%EF%BC%89.jpg',
                                    title='今天想吃什麼呢?',
                                    text='請選擇美食類別',
                                    actions=[
                                            PostbackTemplateAction(
                                            label='約會餐廳',
                                            text='約會餐廳',
                                            data='D&約會餐廳'
                                            ),
                                            PostbackTemplateAction(
                                            label='酒吧',
                                            text='酒吧',
                                            data='D&酒吧'
                                            ),
                                            PostbackTemplateAction(
                                            label='甜點',
                                            text='甜點',
                                            data='D&甜點'
                                            )
                                        ]
                                    ),
                                    CarouselColumn(
                                    thumbnail_image_url='https://www.gomaji.com/blog/wp-content/uploads/2021/08/210808305_533477061180285_3342937421003953170_n-e1630248285751.jpg',
                                    title='今天想吃什麼呢?',
                                    text='請選擇美食類別',
                                    actions=[
                                            PostbackTemplateAction(
                                            label='小吃',
                                            text='小吃',
                                            data='D&小吃'
                                            ),
                                            PostbackTemplateAction(
                                            label='宵夜',
                                            text='宵夜',
                                            data='D&宵夜'
                                            ),
                                            PostbackTemplateAction(
                                            label='早午餐',
                                            text='早午餐',
                                            data='D&早午餐'
                                            )
                                        ]
                                    ),
                                        CarouselColumn(
                                    thumbnail_image_url='https://lh3.googleusercontent.com/s-kh-ArDC85xuSPH8OJso2TkN9CkOJu9B1kDVUWjxkXBZupciCpZAF84CglQxOGvSxwDWTkHdgO84aBsNq2V4bI9w9ukQwp0zg2h9Kn5iLQ8=s600',
                                    title='今天想吃什麼呢?',
                                    text='請選擇美食類別',
                                    actions=[
                                            PostbackTemplateAction(
                                            label='健康餐盒',
                                            text='健康餐盒',
                                            data='D&健康餐盒'
                                            ),
                                            PostbackTemplateAction(
                                            label='素食',
                                            text='素食',
                                            data='D&素食'
                                            ),
                                            PostbackTemplateAction(
                                            label='咖啡',
                                            text='咖啡',
                                            data='D&咖啡'
                                            )
                                        ]
                                    )
                                ]
                            )
                        )
        return Carousel_templatecate
# 「選擇消費價格」按鈕樣板訊息
class PriceMessage(Message):
    def __init__(self, category):
        self.category = category

    def content(self):
        body = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='Menu',
                text='請選擇消費金額',
                actions=[
                    PostbackTemplateAction(
                        label='150以內',
                        text='150以內',
                        data='C&' + self.category + '&1'
                    ),
                    PostbackTemplateAction(
                        label='150-600',
                        text='150-600',
                        data='C&' + self.category + '&2'
                    ),
                    PostbackTemplateAction(
                        label='600-1200',
                        text='600-1200',
                        data='C&' + self.category + '&3'
                    ),
                    PostbackTemplateAction(
                        label='1200以上',
                        text='1200以上',
                        data='C&' + self.category + '&4'
                    )
                ]
            )
        )
        return body

class CategoryMessage(Message): # 如果回傳值為「選擇地區」回復「選擇美食類別」按鈕樣板訊息
    def __init__(self, area):
        self.area = area 
    def content(self):
        Carousel_templatecate = TemplateSendMessage(
                        alt_text='Carousel template',  #只能塞三個action 每個column數量要一致 最多5個carousel
                        template=CarouselTemplate(
                        columns=[
                                CarouselColumn(
                                    thumbnail_image_url='https://www.welcometw.com/wp-content/uploads/2020/11/%E8%80%81%E9%BC%8E%E6%97%BA-1-825x510.jpg',
                                    title='今天想吃什麼呢?',
                                    text='請選擇美食類別',
                                    actions=[
                                            PostbackTemplateAction(
                                            label='火鍋',
                                            text='火鍋',
                                            data='B&' + self.area + '&火鍋'
                                            ),
                                            PostbackTemplateAction(
                                            label='燒烤',
                                            text='燒烤',
                                            data='B&' + self.area + '&燒烤'
                                            ),
                                            PostbackTemplateAction(
                                            label='吃到飽',
                                            text='吃到飽',
                                            data='B&' + self.area + '&吃到飽'
                                            )
                                        ]
                                    ),
                                    CarouselColumn(
                                    thumbnail_image_url='https://doqvf81n9htmm.cloudfront.net/data/jamiesu_149/2020SEP/0904/DF4.jpg',
                                    title='今天想吃什麼呢?',
                                    text='請選擇美食類別',
                                    actions=[
                                            PostbackTemplateAction(
                                            label='日式料理',
                                            text='日式料理',
                                            data='B&' + self.area + '&日式料理'
                                            ),
                                            PostbackTemplateAction(
                                            label='韓式料理',
                                            text='韓式料理',
                                            data='B&' + self.area + '&韓式料理'
                                            ),
                                            PostbackTemplateAction(
                                            label='拉麵',
                                            text='拉麵',
                                            data='B&' + self.area + '&拉麵'
                                            )
                                        ]
                                    ),
                                    CarouselColumn(
                                    thumbnail_image_url='https://wowlavie-aws.hmgcdn.com/file/article_all/%E4%B8%80%E6%A8%93%E8%A5%BF%E5%BC%8F%E6%8B%B1%E5%BD%A2%E9%85%92%E6%9E%B6%E6%93%BA%E7%BD%AE%E4%BA%86%E8%A8%B1%E5%A4%9A%E5%BA%97%E5%85%A7%E9%85%92%E6%AC%BE%E3%80%81%E5%85%AC%E4%BB%94%E6%94%B6%E8%97%8F%EF%BC%88%E5%81%B4%E9%82%8A%EF%BC%89.jpg',
                                    title='今天想吃什麼呢?',
                                    text='請選擇美食類別',
                                    actions=[
                                            PostbackTemplateAction(
                                            label='約會餐廳',
                                            text='約會餐廳',
                                            data='B&' + self.area + '&約會餐廳'
                                            ),
                                            PostbackTemplateAction(
                                            label='酒吧',
                                            text='酒吧',
                                            data='B&' + self.area + '&酒吧'
                                            ),
                                            PostbackTemplateAction(
                                            label='甜點',
                                            text='甜點',
                                            data='B&' + self.area + '&甜點'
                                            )
                                        ]
                                    ),
                                    CarouselColumn(
                                    thumbnail_image_url='https://www.gomaji.com/blog/wp-content/uploads/2021/08/210808305_533477061180285_3342937421003953170_n-e1630248285751.jpg',
                                    title='今天想吃什麼呢?',
                                    text='請選擇美食類別',
                                    actions=[
                                            PostbackTemplateAction(
                                            label='小吃',
                                            text='小吃',
                                            data='B&' + self.area + '&小吃'
                                            ),
                                            PostbackTemplateAction(
                                            label='宵夜',
                                            text='宵夜',
                                            data='B&' + self.area + '&宵夜'
                                            ),
                                            PostbackTemplateAction(
                                            label='早午餐',
                                            text='早午餐',
                                            data='B&' + self.area + '&早午餐'
                                            )
                                        ]
                                    ),
                                     CarouselColumn(
                                    thumbnail_image_url='https://lh3.googleusercontent.com/s-kh-ArDC85xuSPH8OJso2TkN9CkOJu9B1kDVUWjxkXBZupciCpZAF84CglQxOGvSxwDWTkHdgO84aBsNq2V4bI9w9ukQwp0zg2h9Kn5iLQ8=s600',
                                    title='今天想吃什麼呢?',
                                    text='請選擇美食類別',
                                    actions=[
                                            PostbackTemplateAction(
                                            label='健康餐盒',
                                            text='健康餐盒',
                                            data='B&' + self.area + '&健康餐盒'
                                            ),
                                            PostbackTemplateAction(
                                            label='素食',
                                            text='素食',
                                            data='B&' + self.area + '&素食'
                                            ),
                                            PostbackTemplateAction(
                                            label='咖啡',
                                            text='咖啡',
                                            data='B&' + self.area + '&咖啡'
                                            )
                                        ]
                                    )
                                ]
                            )
                        )
        return Carousel_templatecate





import requests
import json
import urllib
import time
import random

GOOGLE_API_KEY = 'AIzaSyBNJF0jfTo28cI4eFHXjn5DmbxVr8d9paM'

def randomget(address):
    # decode url
    address = urllib.request.quote(address)
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address + '&key=' + GOOGLE_API_KEY
    
    while True:
        res = requests.get(url)
        js = json.loads(res.text)
        if js["status"] != "OVER_QUERY_LIMIT":
            time.sleep(1)
            break
    result = js["results"][0]["geometry"]["location"]
    #print(latitude,longitude)
    lat = result["lat"]
    lng = result["lng"]
    nearby_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={}&location={},{}&rankby=distance&type=restaurant&language=zh-TW".format(GOOGLE_API_KEY, lat, lng)
    nearby_results = requests.get(nearby_url)
    # 2. 得到最近的20間餐廳
    nearby_restaurants_dict = nearby_results.json()
    top20_restaurants = nearby_restaurants_dict["results"]
    ## CUSTOMe choose rate >= 4
    res_num = (len(top20_restaurants)) ##20
    above4=[]
    for i in range(res_num):
        try:
            if top20_restaurants[i]['rating'] > 3.9:
                #print('rate: ', top20_restaurants[i]['rating'])
                above4.append(i)
        except:
            KeyError
    if len(above4) < 0:
        print('沒有4星的餐廳')
    # 3. 隨機選擇一間餐廳
        restaurant = random.choice(top20_restaurants)
    restaurant = top20_restaurants[random.choice(above4)]
    # 4. 檢查餐廳有沒有照片，有的話會顯示
    if restaurant.get("photos") is None:
        thumbnail_image_url = None
    else:
        # 根據文件，最多只會有一張照片
        photo_reference = restaurant["photos"][0]["photo_reference"]
        thumbnail_image_url = "https://maps.googleapis.com/maps/api/place/photo?key={}&photoreference={}&maxwidth=1024".format(GOOGLE_API_KEY, photo_reference)
    # 5. 組裝餐廳詳細資訊
    rating = "無" if restaurant.get("rating") is None else restaurant["rating"]
    address = "沒有資料" if restaurant.get("vicinity") is None else restaurant["vicinity"]
    details = "南瓜評分：{}\n南瓜地址：{}".format(rating, address)

    # 6. 取得餐廳的 Google map 網址
    map_url = "https://www.google.com/maps/search/?api=1&query={lat},{long}&query_place_id={place_id}".format(
        lat=restaurant["geometry"]["location"]["lat"],
        long=restaurant["geometry"]["location"]["lng"],
        place_id=restaurant["place_id"]
    )
    buttons_template_message = TemplateSendMessage(
            alt_text=restaurant["name"],
            template=ButtonsTemplate(
                thumbnail_image_url=thumbnail_image_url,
                title=restaurant["name"],
                text=details,
                actions=[
                    URITemplateAction(
                        label='查看地圖',
                        uri=map_url
                    ),
                ]
            )
        )
    return buttons_template_message