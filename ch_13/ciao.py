from urllib import request, parse, error
import json

serviceurl = "http://api.weatherapi.com/v1/current.json"

api_key = "70054fa919c448b7992132453231809"

query_params = parse.urlencode({"key":api_key,"q":"Ferrandina"})

print(query_params)

url = f"{serviceurl}?{query_params}"
print(url)

uh = request.urlopen(url)

data = uh.read().decode()

js = json.loads(data)
print(js)

