from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import os 

Data_Frames = []
teams = ["SAS","LAL","BOS","CHI"]
start = input()
finish = input()
for year in range(int(start),int(finish)+1):
    year = str(year)
    for team in teams:
        url = f"https://www.basketball-reference.com/teams/{team}/{year}.html"
        print(url)
        doc = requests.get(url)
        soup = BeautifulSoup(doc.text, "html.parser")
        try:
            body = soup.find(name = "table", attrs = {"id" : "per_game"}).tbody
        except:
            continue
        rows = body.find_all(name = "tr")

        lst_of_totals = list()
        for row in rows:
            lst = list()
            stats = row.find_all("td")
            for stat in stats:
                stat = stat.text
                lst.append(stat)
            lst_of_totals.append(lst)

        data_set  = {"Player": [n[0] for n in lst_of_totals], "Age" : [n[1] for n in lst_of_totals], "G":[n[2] for n in lst_of_totals], "GS" : [n[3] for n in lst_of_totals],
                    "MP": [n[4] for n in lst_of_totals], "FG":[n[5] for n in lst_of_totals], "FGA": [n[6] for n in lst_of_totals],"FG%":[n[7] for n in lst_of_totals],
                    "3P":[n[8] for n in lst_of_totals],"3PA":[n[9] for n in lst_of_totals],"3P%":[n[10] for n in lst_of_totals],"2P":[n[11] for n in lst_of_totals],
                    "2PA":[n[12] for n in lst_of_totals],"2P%":[n[13] for n in lst_of_totals],"eFG%":[n[14] for n in lst_of_totals],"FT":[n[15] for n in lst_of_totals],
                    "FTA": [n[16] for n in lst_of_totals],"FT%":[n[17] for n in lst_of_totals],"ORB":[n[18] for n in lst_of_totals],"DRB":[n[19] for n in lst_of_totals],
                    "TRB":[n[20] for n in lst_of_totals],"AST":[n[21] for n in lst_of_totals],"STL":[n[22] for n in lst_of_totals],"BLK":[n[23] for n in lst_of_totals],
                    "TOV":[n[24] for n in lst_of_totals],"PF":[n[25] for n in lst_of_totals],"PTS":[n[26] for n in lst_of_totals]}

        df = pd.DataFrame(data_set)
        try:
            os.makedirs(f".\\final prog\\{team}\\{team}_{year}")
        except:
            time.sleep(4)
            continue
        df.to_csv(f".\\final prog\\{team}\\{team}_{year}\\{team}_{year}_table.csv")
        
        time.sleep(4)



