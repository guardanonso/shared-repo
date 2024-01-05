import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.basketball-reference.com/leagues/NBA_2023_advanced.html"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find("tbody").find_all(name = "tr", class_ = "full_table")

lst_of_totals = []
for row in rows:
    lst = []
    stats = row.find_all("td")
    for stat in stats:
        lst.append(stat.text)
    lst_of_totals.append(lst)

data_frame = {"Player":[n[0]for n in lst_of_totals],"Pos": [n[1]for n in lst_of_totals]}

df = pd.DataFrame(data_frame)
pd.set_option("display.max_rows", None)
print(df)