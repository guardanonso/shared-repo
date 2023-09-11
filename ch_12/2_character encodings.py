from urllib.request import urlopen

with urlopen("https://www.example.com") as response:
    body = response.read()
print(dir(response.headers))
charset = response.headers.get_content_charset()

print(charset)
decoded_body = body.decode(charset)

print(decoded_body)

