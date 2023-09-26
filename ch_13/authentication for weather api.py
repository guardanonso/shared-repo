import requests
<<<<<<< HEAD
from bs4 import BeautifulSoup

login = "flavio.marolla1@gmail.com"
password = "Ciaoiosonosveva1"

data = {"login" : login,
        "password" : password,}
=======

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

>>>>>>> f57f032d4656b65be6b2ee74e79c139aa3bf8d72
