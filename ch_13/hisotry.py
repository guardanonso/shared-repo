from urllib import request, parse, error
import json
from datetime import date, datetime, timedelta


history_url = "http://api.weatherapi.com/v1/history.json"
api_key = "70054fa919c448b7992132453231809"
location = input("Enter a location: ")

while True:
    days = input("How many days behind?: ")
    if days.isdigit() and float(str(days)).is_integer() and 1 < int(days) <= 365:
        break
    else:   continue

dates_lst = list()
for n in range(1,int(days)+1):
    tod = date.today()
    date_format = "%Y-%m-%d"
    dtObj = datetime.strptime(str(tod), date_format)
    past_date = dtObj - timedelta(days=n) 
    dates = str(past_date.date())
    dates_lst.append(dates)

def history_weather_data(api_url):
    temp_lst = list()
    for d in dates_lst:
        query_params = parse.urlencode({"key":api_key,"q":location, "dt" : d})
        url = f"{api_url}?{query_params}"

        try:
            with request.urlopen(url, timeout = 10) as uh:
                data = uh.read().decode()
                dic = json.loads(data)
                avgtemp_c = dic["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
                city_name = dic["location"]["name"]
                temp_lst.append(avgtemp_c)
                print(d, avgtemp_c, "°C")
                
        except error.HTTPError as err:
            print(err)
            quit()
        except error.URLError as err:
            print(err)
            quit()
        except TimeoutError as err:
            print(err)
            quit()
    print(f"The avarage temperature in the city of {city_name} was {round((sum(temp_lst)/len(temp_lst)), 1)} °C")
    
history_weather_data(history_url)
