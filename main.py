from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']
yutianday = os.environ['YUTIANDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]


now_time = today.now()                                               
week_day = today.isoweekday()                                        
week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天']             
text_date = '今天是[' + str(now_time)[0:10] + ']' + week[week_day - 1]   


def get_weather():
  url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
  res = requests.get(url).json()
  weather = res['data']['list'][0]
  return weather['weather'], math.floor(weather['temp'])


def get_weaher2():                                                                                                               
    url = "https://v0.yiketianqi.com/api?unescape=1&version=v61&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city=" + city     
    res = requests.get(url).json()                                                                                               
    return res['city'], res['wea'], res['tem1'], res['tem2'], res['humidity'], res['air_level'], res['air_tips']                 

def get_yutian():
  delta = today - datetime.strptime(yutianday, "%Y-%m-%d")
  return delta.days

def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days

def get_birthday():
  next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days

def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
# wea, temerature = get_weather()
# data = {"weather":{"value":wea},"temperature":{"value":temperature},"love_days":{"value":get_count()},"yutian_days":{"value":get_yutian()},"birthday_left":{"value":get_birthday()},"words":{"value":get_words(), "color":get_random_color()}}

res_city, wea, high, low, humidity, air_level, air_tips = get_weaher2() 
data = {"air_tips": {"value": air_tips}, "air_level": {"value": air_level}, "text_date": {"value": text_date},         
        "humidity": {"value": humidity, "color": get_random_color()},                                                  
        "city": {"value": res_city, "color": get_random_color()}, "weathr": {"value": wea, "color": get_random_color()},                            
        "low": {"value": low, "color": get_random_color()}, "high": {"value": high, "color": get_random_color()},      
        "love_days": {"value": get_count()}, "birthday_left": {"value": get_birthday()},                               
        "words": {"value": get_words(), "color": get_random_color()}}                                                  

user_ids=user_id.split(",")
for userid in user_ids:
  res = wm.send_template(userid, template_id, data)
  print(res)
