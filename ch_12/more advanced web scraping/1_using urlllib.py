from urllib.request import urlopen

# trattato come un file object,
#  ricordare di chiuderlo, con context manager
with urlopen("https://www.example.com") as response:
    body = response.read()
# oppure esplicitamente
response = urlopen("https://www.example.com")
body = response.read()#.decode() per ottenre str object da bytes object
response.close()
print(type(body))
print(body)

# interagire con headers e altre cose
print(type(body))
headers = response.getheaders()
print(headers)
print(response.getheader("Server"))

