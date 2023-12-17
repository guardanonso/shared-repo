from bs4 import BeautifulSoup
import requests

url = "https://www.basketball-reference.com/teams/BOS/2024.html"

doc = requests.get(url)
soup = BeautifulSoup(doc.text, "html.parser")

# print(soup.prettify)

body  = soup.find("table", attrs = {"id" : "per_game"}).tbody
result = []

rows = body.find_all(name = "tr")
dic  =  dict()

for row in rows:
    lst = list()
    stats = row.find_all("td")
    for stat in stats:
        if  stat is stats[0]:
            name = stat.text
        else:
            stat = stat.text
            lst.append(stat)
    dic.update({name : lst})

print(dic)
            


