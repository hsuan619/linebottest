import requests
import urllib.request
import json
import time
import googlemaps

GOOGLE_API_KEY = 'AIzaSyBNJF0jfTo28cI4eFHXjn5DmbxVr8d9paM'

def get_latitude_longtitude(address):
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
    print(lat,lng)
    return lat, lng



def find(category):
    address = get_latitude_longtitude(address)
    
    rad = 500
    loc = get_latitude_longtitude(address)
    print(loc)
    gmaps=googlemaps.Client(key=GOOGLE_API_KEY)
    gmaps.places_radar(keyword=category,location=loc, radius=rad)['results'] #餐廳

    pids=[]
    for place in gmaps.places_radar(keyword=category, location=loc, radius=rad)['results']:
        pids.append(place['place_id'])
    restaurant_info = []
    for id in pids:
        print ("running")
    restaurant_info.append(gmaps.place(place_id=id, language='zh-TW')['result'])
    #每次間隔0.3sec
    time.sleep(0.3)
    print (restaurant_info[0])


