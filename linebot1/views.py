
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
 
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
from .scraper import IFoodie
from .messages import *
from line import settings

import requests
import json

import time
import random





line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
GOOGLE_API_KEY = 'AIzaSyBNJF0jfTo28cI4eFHXjn5DmbxVr8d9paM'

@csrf_exempt
def callback(request):
    
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        
        
        for event in events:

            if isinstance(event, MessageEvent):  # 如果有訊息事件

                if event.message.type=='image':
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text="無法處理圖片訊息\n\n請點擊哈囉左轉愛食記\n或隨機挑選附近餐廳\n(載入需幾秒時間)",quick_reply=QuickReply(items=[QuickReplyButton(action=PostbackAction(label="哈囉", data="哈囉")),QuickReplyButton(action=PostbackAction(label="幫我挑", data="隨便吃"))])))
                elif event.message.type=='video':
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text="無法處理影片訊息\n\n請點擊哈囉左轉愛食記\n或隨機挑選附近餐廳\n(載入需幾秒時間)",quick_reply=QuickReply(items=[QuickReplyButton(action=PostbackAction(label="哈囉", data="哈囉")),QuickReplyButton(action=PostbackAction(label="幫我挑", data="隨便吃"))])))
                elif event.message.type=='sticker':
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='收到你的貼圖囉！\n\n請點擊哈囉左轉愛食記\n或隨機挑選附近餐廳\n(載入需幾秒時間)',quick_reply=QuickReply(items=[QuickReplyButton(action=PostbackAction(label="哈囉", data="哈囉")),QuickReplyButton(action=PostbackAction(label="幫我挑", data="隨便吃"))])))
                elif event.message.type=='location':
                    address = event.message.address
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
                                if top20_restaurants[i]['opening_hours']['open_now'] == True:
                                    above4.append(i)
                        except:
                            KeyError
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
                    open ='非營業中'  if restaurant.get("open_now") is False else '營業中'
                    details = "地址：{}\n{}".format( address,open)
                    name = "{} 評分：{}".format(restaurant["name"],rating)

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
                                title=name,
                                text=details,
                                actions=[
                                    URITemplateAction(
                                        label='查看地圖',
                                        uri=map_url
                                    ),
                                    PostbackAction(
                                        label='再一間',
                                        text = '再一間',
                                        data = '再一間'
                                    )
                                ]
                            )
                        )
                    #'嗨嗨！\n請點擊哈囉左轉愛食記\n或幫你隨機挑選附近餐廳\n(載入需幾秒時間)'
                    line_bot_api.reply_message(event.reply_token,buttons_template_message)
                elif event.message.text=='哈囉':
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請點擊哈囉左轉愛食記\n或隨機挑選附近餐廳\n可以輸入-再一間-重新挑選喔!',quick_reply=QuickReply(items=[QuickReplyButton(action=LocationAction(label="隨便吃")),QuickReplyButton(action=PostbackAction(label="哈囉", data="哈囉"))])))
                elif event.message.text=='再一間':
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='點擊按鈕(載入需幾秒時間)',quick_reply=QuickReply(items=[QuickReplyButton(action=LocationAction(label="再一間")),QuickReplyButton(action=PostbackAction(label="離開", data="離開"))])))
                elif event.message.text=='離開':
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='結束這次查詢，\n請點擊哈囉左轉愛食記\n或隨機挑選附近餐廳',quick_reply=QuickReply(items=[QuickReplyButton(action=LocationAction(label="隨便吃")),QuickReplyButton(action=PostbackAction(label="哈囉", data="哈囉"))])))
            elif isinstance(event, PostbackEvent):  # 如果有回傳值事件 '若要隨機選擇請點擊按鈕'
                if event.postback.data[0:1] == "A":
                    line_bot_api.reply_message(   # 回復「選擇美食類別」按鈕樣板訊息
                        event.reply_token,
                        CategoryMessage(event.postback.data[2:]).content()
                    ) # 回復「選擇美食類別」按鈕樣板訊息
                elif event.postback.data[0:1] == "B":  # 如果回傳值為「選擇美食類別」

                    line_bot_api.reply_message(   # 回復「選擇消費金額」按鈕樣板訊息
                        event.reply_token,
                        PriceMessage(event.postback.data[2:]).content()
                    )
                elif event.postback.data[0:1] == "C":  # 如果回傳值為「選擇消費金額」

                    result = event.postback.data[2:].split('&')  # 回傳值的字串切割

                    food = IFoodie(
                        result[0],  # 地區
                        result[1],   #類別
                        result[2]   #price
                    )
                    line_bot_api.reply_message(  # 回復訊息文字
                        event.reply_token,TextSendMessage(text=food.scrape(),quick_reply=QuickReply(items=[QuickReplyButton(action=PostbackAction(label="離開", data="離開"))])))
                    # 爬取該地區正在營業，且符合所選擇的美食類別及消費價格的前五大最高人氣餐廳
                elif event.postback.data == "離開":
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='結束這次查詢，\n請點擊哈囉左轉愛食記\n或隨機挑選附近餐廳',quick_reply=QuickReply(items=[QuickReplyButton(action=PostbackAction(label="幫我挑", data="再一間")),QuickReplyButton(action=PostbackAction(label="哈囉", data="哈囉"))])))
                elif event.postback.data == "哈囉":
                    line_bot_api.reply_message(event.reply_token,AreaMessage().content())
                
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
