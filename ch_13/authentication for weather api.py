import requests

URL = "https://www.weatherapi.com"
playload = {"ctl00$MainContentHolder$Login1$UserName" : "flavio.marolla1@gmail.com",
            "ctl00$MainContentHolder$Login1$Password" : "Ciaoiosonosveva1"}
s = requests.session()

response = s.post(URL, playload)

content = response.content

print(response.status_code)

print(content)

with open("non so.html","wb") as file:
    file.write(content)

