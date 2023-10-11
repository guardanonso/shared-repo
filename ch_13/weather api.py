from urllib import parse, request
from urllib.error import URLError, HTTPError
import json
from datetime import date, datetime, timedelta

inp = input("Choose between\n(1)Current weather\n(2)\nType the assigned number (1 or 2)")
location = input()
if inp == "2":
    dates_lst = list()
    while True:
        days = input()
        try:
            int(days)
        except:
            print("Enter a number")
            continue
        if int(days) <= 8:  break
        else:   continue

    for n in range(1,int(days)+1):
        tod = date.today()
        date_format = "%Y-%m-%d"
        dtObj = datetime.strptime(str(tod), date_format)
        past_date = dtObj - timedelta(days=n) 
        dates = str(past_date.date())
        dates_lst.append(dates)

    def weather_api(city):
        key = "70054fa919c448b7992132453231809"
        base_url = "http://api.weatherapi.com/v1/history.json"

        for d in dates_lst:
            humidity_list = list()
            chance_list = list()

            for n in range(0,24):
                try:
                    query_params = parse.urlencode({"key" : key, "q" : city, "dt" : d, "hour" : str(n)})
                    url = f"{base_url}?{query_params}"
                    with request.urlopen(url) as req:
                        dic = json.loads(req.read().decode())
                        chance_of_rain = dic["forecast"]["forecastday"][0]["hour"][0]["chance_of_rain"]
                        humidity = dic["forecast"]["forecastday"][0]["hour"][0]["humidity"]
                        a = dic["forecast"]["forecastday"][0]["day"]["avghumidity"]
                        avgtemp_c = dic["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
                        chance_list.append(chance_of_rain)
                        humidity_list.append(humidity)
                        avg_chance_of_rain = sum(chance_list)/len(chance_list)
                        avg_humidity = sum(humidity_list)/len(humidity_list)
                except HTTPError as err:
                    print(err)
                    quit()
                except URLError as err:
                    print(err)
                    quit()
            
            print(d, round(avg_humidity, 1),avgtemp_c, round(avg_chance_of_rain,1))
    weather_api(location)
elif inp == "1":
    def current_weather_data(location):
        current_url = "http://api.weatherapi.com/v1/current.json"
        api_key = "70054fa919c448b7992132453231809"

        query_params = parse.urlencode({"key":api_key,"q" : location})
        url = f"{current_url}?{query_params}"
        try:
            with request.urlopen(url) as uh:
                data = uh.read().decode()
                dic = json.loads(data)
                humidity = dic["current"]["humidity"]
                temp = dic["current"]["feelslike_c"]
 
        except HTTPError as err:
            print(err)
            quit()
        except URLError as err:
            print(err)
            quit()
        print(humidity, temp)
    current_weather_data(location)








