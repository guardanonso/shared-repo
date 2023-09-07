import socket
import re

# Given a URL
url = "https://www.aranzulla.it/wp-content/contenuti/2016/08/ad5972a7.jpg"

# Use regular expression to extract host and path of the file
match = re.match(r"https://([^/]+)/(.+)", url)
if match:
    HOST = match.group(1)
    PATH = "/" + match.group(2)
else:
    print("Invalid URL format")
    exit()

# Create a socket and connect it to the host
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, 80))

# Send request to the server
request = f"GET {PATH} HTTP/1.1\r\nHost: {HOST}\r\n\r\n"
mysock.send(request.encode())

response = b""
while True:
    data = mysock.recv(1024)
    if not data:
        break
    response += data
print(response)
# Close the socket
mysock.close()

# Save the downloaded data to a file
with open("downloaded_image.jpg", "wb") as fhand:
    fhand.write(response)

print("Image downloaded successfully!")