from bs4 import BeautifulSoup
import requests

url = f"https://www.basketball-reference.com/teams/BOS/2024.html"
doc = requests.get(url)

with open("doc.html", "w", encoding = "utf-8") as f:
    f.write(doc.text)

with open("doc.html", "r", encoding = "utf-8") as f:
    soup = BeautifulSoup(f,"html.parser")

tag = soup.find_all(name = "table", attrs = {"id" : "per_game"})

for a in tag:
    print(a.text)
