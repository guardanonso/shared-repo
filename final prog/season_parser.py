import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import regex

url = "https://www.basketball-reference.com/leagues/NBA_2023_per_game.html"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find("tbody").find_all(name = "tr", class_ = "full_table")
href_lst = []
lst_of_totals = []
for row in rows:
    lst = []
    stats = row.find_all("td")
    links = row.find_all("a")
    for link in links:
        href = link.get("href")
        if "players" in href:
            href_lst.append(href)
    for stat in stats:
        lst.append(stat.text)
    lst_of_totals.append(lst)

time.sleep(4)

url = f"https://www.basketball-reference.com/players/l/lowryky01.html"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
idk = soup.find(name="div",id="meta").find_all("p")
print(idk[3].text)

data_frame = {
            "Player":[n[0]for n in lst_of_totals],"Pos": [n[1]for n in lst_of_totals],"Age":[n[2]for n in lst_of_totals],"Tm":[n[3]for n in lst_of_totals],
            "G":[n[4]for n in lst_of_totals],"GS": [n[5]for n in lst_of_totals], "MP":[n[6]for n in lst_of_totals],"FG":[n[7]for n in lst_of_totals],
            "FGA":[n[8]for n in lst_of_totals],"FG%":[n[9]for n in lst_of_totals],"3P":[n[10]for n in lst_of_totals], "3PA":[n[11]for n in lst_of_totals],
            "3P%":[n[12]for n in lst_of_totals],"2P":[n[13]for n in lst_of_totals],"2PA":[n[14]for n in lst_of_totals],"2P%": [n[15]for n in lst_of_totals],
            "eFG%":[n[16]for n in lst_of_totals],"FT":[n[17]for n in lst_of_totals],"FTA":[n[18]for n in lst_of_totals],"FT%":[n[19]for n in lst_of_totals],
            "ORB":[n[20]for n in lst_of_totals],"DRB":[n[21]for n in lst_of_totals],"TRB":[n[22]for n in lst_of_totals],"AST":[n[23]for n in lst_of_totals],
            "STL":[n[24]for n in lst_of_totals],"BLK":[n[25]for n in lst_of_totals],"TOV":[n[26]for n in lst_of_totals],"PF":[n[27]for n in lst_of_totals],
            "PTS":[n[28]for n in lst_of_totals]
            }

players_names = [n[0] for n in lst_of_totals]

df = pd.DataFrame(data_frame)
print(href_lst[299])

# df.to_csv(".\\final prog\\season_table.csv")