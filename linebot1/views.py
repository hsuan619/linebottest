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

#git add .
#git commit -m "your_message"
#heroku git:remote -a foodieline
#git push heroku master

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


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
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text="無法處理圖片訊息\n\n請輸入哈囉或點擊按鈕尋找附近餐廳",quick_reply=QuickReply(items=[QuickReplyButton(action=PostbackAction(label="哈囉", data="哈囉")),QuickReplyButton(action=LocationAction(label="傳送位置"))])))
                elif event.message.type=='video':
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text="無法處理影片訊息\n\n請輸入哈囉或點擊按鈕尋找附近餐廳",quick_reply=QuickReply(items=[QuickReplyButton(action=PostbackAction(label="哈囉", data="哈囉")),QuickReplyButton(action=LocationAction(label="傳送位置"))])))
                elif event.message.type=='sticker':
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='收到你的貼圖囉！\n\n請輸入哈囉或點擊按鈕尋找附近餐廳',quick_reply=QuickReply(items=[QuickReplyButton(action=PostbackAction(label="哈囉", data="哈囉")),QuickReplyButton(action=LocationAction(label="傳送位置"))])))
                elif event.message.type=='location':
                    address = event.message.address
                    line_bot_api.reply_message(event.reply_token,getnearby())
                    line_bot_api.reply_message(event.reply_token,aother())
                    if event.message.text=='隨便吃':
                            line_bot_api.reply_message(event.reply_token,randomget(address))
                            line_bot_api.reply_message(event.reply_token,aother())
            elif isinstance(event, PostbackEvent):  # 如果有回傳值事件
                if event.postback.data == "哈囉":
                    line_bot_api.reply_message(event.reply_token,AreaMessage().content())
                elif event.postback.data == "關鍵字":
                    line_bot_api.reply_message(   # 回復「選擇美食類別」按鈕樣板訊息
                        event.reply_token,
                        Category2Message(event.postback.data[2:]).content() #回復類別
                    )
                elif event.postback.data == "新的":
                    line_bot_api.reply_message(event.reply_token,randomget(address))
                elif event.postback.data[0:1] == "D":  #location
                    #result2 = event.postback.data[2:].split('&')
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='結束這次查詢，\n請再次輸入 哈囉\n或點擊按鈕尋找附近餐廳',quick_reply=QuickReply(items=[QuickReplyButton(action=LocationAction(label="傳送我的位置"))])))
                elif event.postback.data[0:1] == "A":
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
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='結束這次查詢，\n請再次輸入 哈囉\n或點擊按鈕尋找附近餐廳',quick_reply=QuickReply(items=[QuickReplyButton(action=LocationAction(label="傳送我的位置"))])))
            
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
