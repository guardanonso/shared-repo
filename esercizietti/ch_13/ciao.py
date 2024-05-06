from urllib import request, parse, error
import json
from datetime import date, datetime
from datetime import timedelta

# inp = input("Choose between these options:\n1. Current weather in a given location \n2. Forecast weather\n3. History weather(previous 7 days in a given location)")
current_url = "http://api.weatherapi.com/v1/current.json"

api_key = "70054fa919c448b7992132453231809"
location = input("Enter a location: ")


def current_weather_data(api_url):

    query_params = parse.urlencode({"key":api_key,"q" : location})
    print(query_params)

    url = f"{api_url}?{query_params}"

    try:
        with request.urlopen(url) as uh:
            data = uh.read().decode()
            dic = json.loads(data)
        print(json.dumps(dic, indent = 4))

    except error.HTTPError as err:
        print(err)
    except error.URLError as err:
        print(err)

print(current_weather_data(current_url))






