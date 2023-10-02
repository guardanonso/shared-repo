from urllib import request, error, parse
import json
from datetime import date, datetime, timedelta

dates_lst = list()

days = "3"
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
        for n in range(0,24):
            query_params = parse.urlencode({"key" : key, "q" : city, "dt" : d, "hour" : str(n)})
            url = f"{base_url}?{query_params}"

            with request.urlopen(url) as req:
                dic = json.loads(req.read().decode())
                chance_of_rain = dic["forecast"]["forecastday"][0]["hour"][0]["chance_of_rain"]
                humidity = dic["forecast"]["forecastday"][0]["hour"][0]["humidity"]
                a = dic["forecast"]["forecastday"][0]["day"]["avghumidity"]
                humidity_list = list()
                chance_list = list()
                chance_list.append(chance_of_rain)
                humidity_list.append(humidity)
                avg_chance_of_rain = sum(chance_list)/len(chance_list)
                avg_humidity = sum(humidity_list)/len(humidity_list)
        print(avg_chance_of_rain, avg_humidity, a)
    return(dic)

a = "rome"
print(weather_api(a))




