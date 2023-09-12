from urllib.request import urlopen
from urllib.error import URLError, HTTPError

myurl = input("Enter a URL: ")
def make_request(url):
    with urlopen(url, timeout=10) as response:
        print(response.status)
        return(response.read(),response)
make_request(myurl)