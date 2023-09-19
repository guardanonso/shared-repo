from urllib import request, parse, error
import json
from datetime import date, datetime
from datetime import timedelta

history_url = "http://api.weatherapi.com/v1/history.json"
api_key = "70054fa919c448b7992132453231809"
location = input("Enter a location: ")

while True:
    days = input("How many days behind?: ")
    if days.isdigit() and float(str(days)).is_integer() and int(days)<= 365:
        break
    else:   continue

lst = list()
for n in range(1,int(days)+1):
    tod = date.today()
    date_format = "%Y-%m-%d"
    dtObj = datetime.strptime(str(tod), date_format)
    past_date = dtObj - timedelta(days=n) 
    dates = str(past_date.date())
    print(dates,type(dates))
    lst.append(dates)
print(lst)
    

def history_weather_data(api_url):
    for d in lst:
        query_params = parse.urlencode({"key":api_key,"q":location, "dt" : d})

        url = f"{api_url}?{query_params}"

        try:
            with request.urlopen(url,timeout=10) as uh:
                data = uh.read().decode()
                dic = json.loads(data)
                avgtemp_c = dic["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
                print(avgtemp_c, type(avgtemp_c))

        except error.HTTPError as error:
            print(error)
        except error.URLError as error:
            print(error)
        except TimeoutError as error:
            print(error)

history_weather_data(history_url)
