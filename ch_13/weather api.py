from urllib import request, error, parse
import json

def weather_api(city):
    key = "70054fa919c448b7992132453231809"
    base_url = "http://api.weatherapi.com/v1/history.json"
    
    for n in range(1,24):
        query_params = parse.urlencode({"key" : key, "q" : city, "dt" : "2023-09-26", "hour" : str(n)})
        url = f"{base_url}?{query_params}"

        with request.urlopen(url) as req:
            dic = json.loads(req.read().decode())
            print(type(dic))
    return(dic)

a = "romeo"
print(weather_api(a))




