import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.basketball-reference.com/leagues/NBA_2024_per_game.html"

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
df = pd.DataFrame(data_frame).sort_values(by=['Player']).reset_index()
df.to_csv(".\\final prog\\season_table.csv")

driver = webdriver.Chrome()
driver.get("https://basketball.realgm.com/nba/players")
driver.implicitly_wait(10)
# driver.find_element(By.XPATH, "//select[@onchange='open_network(this.options[this.selectedIndex].value)']").click()
time.sleep(60)
html = driver.page_source
driver.quit()

print(html)

