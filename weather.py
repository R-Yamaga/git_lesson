import requests
import json
from pprint import pprint

API_KEY = "de0493ad02b5f68f7866c1ea3a8819e4"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?units=metric&lang=ja"
city = "Kobe,jp"

response = requests.get(BASE_URL + "&q={}&APPID={}".format(city, API_KEY))
weather_data = json.loads(response.text)
# pprint(weather_data)

city = weather_data['name']
weather = weather_data['weather'][0]['description']

result = "{}の天気は{}です。".format(city, weather)

print(result)