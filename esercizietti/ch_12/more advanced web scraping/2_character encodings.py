from urllib.request import urlopen

# prints the body of the response in a file (html file) if the body uses utf-8 encoding
with urlopen("https://www.example.com") as response:
    body = response.read()
charset = response.headers.get_content_charset()

decoded_body = body.decode(charset)
with open("document.html","wb") as file:
    file.write(body)

# prints the body of the response in a file (html file) if the body uses other kinds of encoding
with urlopen("https://www.google.com") as gresponse:
    gbody = gresponse.read()

gcharset = gresponse.headers.get_content_charset()
print(gcharset)
gdecoded_body = gbody.decode(gcharset)

with open("file2.html", encoding = "iso-8859-1", mode = "w") as gfile:
    gfile.write(gdecoded_body)




