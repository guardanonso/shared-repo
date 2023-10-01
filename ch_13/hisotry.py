from urllib import request, parse, error
import json
from datetime import date, datetime, timedelta


history_url = "http://api.weatherapi.com/v1/history.json"
api_key = "70054fa919c448b7992132453231809"

print("Choose the information you want to retrieve (you can pick more than one) by typing the associated value of the data you are interested in:\n(1) max temperature\n(2) min temperature\n(3) avg temperature\n(4) humidity")
requested_stuff = list()

while True:
    requested_data = input("Please enter a digit: ")
    if requested_data.lower() == "done":
        break
    try:
        i_data = int(requested_data)
    except:
        print("Enter a digit")
        continue
    if i_data <= 3:
        if i_data not in requested_stuff:
            requested_stuff.append(i_data)
    else:   continue

print(requested_stuff)

location = input("Enter a location: ")
dicc = {1 : "maxtemp_c", 2 : "mintemp_c", 3 : "avgtemp_c"} 

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
        query_params = parse.urlencode({"key" : api_key, "q" : location, "dt" : d, "hour" : "23"})
        url = f"{api_url}?{query_params}"

        try:
            with request.urlopen(url, timeout = 10) as uh:
                dic = json.loads(uh.read().decode())
                city_name = dic["location"]["name"]

                avgtemp_c = dic["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
                maxtemp_c = dic["forecast"]["forecastday"][0]["day"]
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
    print(f"The avarage temperature in the city of {city_name} was {round((sum(temp_lst)/len(temp_lst)), 1)} °C in the past {days} days")
    print(json.dumps(dic, indent = 4))
    
history_weather_data(history_url)
