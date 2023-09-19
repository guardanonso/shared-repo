from urllib import request, parse, error
import json
from datetime import date, datetime
from datetime import timedelta

tod = date.today()
date_format = "%Y-%m-%d"
dtObj = datetime.strptime(str(tod), date_format)
past_date = dtObj - timedelta(days=10)

print(past_date.date())

# inp = input("Choose between these options:\n1. Current weather in a given location \n2. Forecast weather\n3. History weather(previous 7 days in a given location)")
current_url = "http://api.weatherapi.com/v1/current.json"
history_url = "http://api.weatherapi.com/v1/history.json"
future_url = "http://api.weatherapi.com/v1/future.json"

url_dic = {"1" : current_url,"2" : history_url, "3" : future_url}

api_key = "70054fa919c448b7992132453231809"
location = input("Enter a location: ")


# def current_weather_data(api_url):

#     query_params = parse.urlencode({"key":api_key,"q" : location})
#     print(query_params)

#     url = f"{api_url}?{query_params}"

#     try:
#         with request.urlopen(url) as uh:
#             data = uh.read().decode()
#             dic = json.loads(data)
#         print(json.dumps(dic, indent = 4))

#     except error.HTTPError as error:
#         print(error)
#     except error.URLError as error:
#         print(error)

def history_weather_data(api_url):
    query_params = parse.urlencode({"key":api_key,"q":location, "dt" : past_date})

    url = f"{api_url}?{query_params}"
    print(url)

    try:
        with request.urlopen(url) as uh:
            data = uh.read().decode()
            dic = json.loads(data)
        print(json.dumps(dic, indent = 4))

    except error.HTTPError as error:
        print(error)
    except error.URLError as error:
        print(error)

history_weather_data(history_url)





