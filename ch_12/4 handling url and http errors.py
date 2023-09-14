from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import json
import ssl

def make_request(url, headers=None):
    request = Request(url, headers = headers or {})
    try: 
        with urlopen(request, timeout=10) as response:
            print(response.status)
            return(response.read(),response)
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print("Request timed out")

body, response = make_request("https://superfish.badssl.com/",
                               {"User-Agent": "Real Python"})
        
print(response.getheaders())


