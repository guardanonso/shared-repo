from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import ssl

url = input("Enter a URL: ")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
try:
    with urlopen(url,context=ctx) as response:
        body = response.read()
        soup = BeautifulSoup(body, "html.parser")
    with open("idk.html", "wb") as file:
        file.write(body)

    list_of_href = list()
    tags = soup("a")
    for tag in tags:
        list_of_href.append(tag.get("href", None))
    print(list_of_href)
except HTTPError as error:
    print(error.status, error.reason)
except URLError as error:
    print(error.reason)



