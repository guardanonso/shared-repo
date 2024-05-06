import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import regex as re
from unidecode import unidecode

MAIN_URL = "https://www.basketball-reference.com/leagues/NBA_2024_per_game.html"
SECOND_URL = "https://basketball.realgm.com/nba/players/2024"

# parsing main url 
response = requests.get(MAIN_URL)
soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find("tbody").find_all(name = "tr", class_ = "full_table")
lst_of_totals = []
for row in rows:
    lst = []
    stats = row.find_all("td")
    for stat in stats:
        stat = stat.text
        lst.append(stat)
    lst_of_totals.append(lst)

# parsing second url
response = requests.get(SECOND_URL)
soup = BeautifulSoup(response.text, "html.parser")
rows = soup.find("tbody").find_all(name = "tr")

totals = []
for row in rows:
    lst = []
    stats = row.find_all("td")
    for stat in stats:
        if "," in stat:
            stat = stat.replace(",","").rstrip()
            lst.append(stat.text)
        lst.append(stat.text)
    totals.append(lst)

# find index of height data
for n in totals[0]:
    x = re.search("\d-\d",n)
    if x:
        position = totals[0].index(n)

# defining a func to convert inches to cm
def feet_to_cm(height):
    feet, inches = height.split('-')
    total_inches = (int(feet) * 12) + int(inches)
    cm = total_inches * 2.54
    return round(cm,1)

# defining a func to convert lbs to kg
def lbs_to_kg(weight):
    kg_weight = int(weight) * .454
    return round(kg_weight,1)

# converting inches to cm
for n in totals:
    height = n[position]
    cm_height = feet_to_cm(height)
    n.remove(height)
    n.insert(position,cm_height)

for n in totals:
    weight = n[position+1]
    kg_weight = lbs_to_kg(weight)
    n.remove(weight)
    n.insert(position+1,kg_weight)

for n in lst_of_totals:
    name = n[0]
    if "*" in name:
        n.remove(name)
        name = name.replace("*", "")
        n.insert(0, name)
    else:   continue

for n in lst_of_totals: 
    for h in totals:
        if n[2]==h[4] and n[3]==h[5] and n[4]==h[6] and unidecode(n[0]) != unidecode(h[0]):
            h.remove(h[0])
            h.insert(0,n[0])

print(len(totals),[unidecode(h[0])for h in totals])
for n in totals:
    print(n[0])


names = []
for n in lst_of_totals: 
    if unidecode(n[0]) in [unidecode(h[0])for h in totals]:
        names.append(n[0])
        for h in totals:
            if unidecode(n[0]) == unidecode(h[0]):
                n.insert(4,h[position])
                n.insert(5,h[position+1])
    else:
        n.insert(4,"None")
        n.insert(5,"None")
        names.append(n[0])
print(len(names))


print(len(totals), len(lst_of_totals), len(names))
print("nigger")
# for n in lst_of_totals:
#     print(len(n))
print(totals[0], lst_of_totals[0])

data_frame = {
            "Player":[n[0]for n in lst_of_totals], "Pos": [n[1]for n in lst_of_totals],"Age":[n[2]for n in lst_of_totals],"Tm":[n[3]for n in lst_of_totals],
            "Height":[n[4]for n in lst_of_totals], "Weight":[n[5]for n in lst_of_totals], "G":[n[6]for n in lst_of_totals],"GS": [n[7]for n in lst_of_totals],
            "MP":[n[8]for n in lst_of_totals],"FG":[n[9]for n in lst_of_totals],"FGA":[n[10]for n in lst_of_totals],"FG%":[n[11]for n in lst_of_totals],
            "3P":[n[12]for n in lst_of_totals], "3PA":[n[13]for n in lst_of_totals],"3P%":[n[14]for n in lst_of_totals],"2P":[n[15]for n in lst_of_totals],
            "2PA":[n[16]for n in lst_of_totals],"2P%": [n[17]for n in lst_of_totals],"eFG%":[n[18]for n in lst_of_totals],"FT":[n[19]for n in lst_of_totals],
            "FTA":[n[20]for n in lst_of_totals],"FT%":[n[21]for n in lst_of_totals],"ORB":[n[22]for n in lst_of_totals],"DRB":[n[23]for n in lst_of_totals],
            "TRB":[n[24]for n in lst_of_totals],"AST":[n[25]for n in lst_of_totals],"STL":[n[26]for n in lst_of_totals],"BLK":[n[27]for n in lst_of_totals],
            "TOV":[n[28]for n in lst_of_totals],"PF":[n[29]for n in lst_of_totals], "PTS":[n[30]for n in lst_of_totals]
            }

df = pd.DataFrame(data_frame).sort_values(by=['Player']).reset_index()
df.to_csv(".\\final prog\\season_table.csv")


