from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import os 

Data_Frames = []
teams = ["SAS","LAL","BOS","CHI"]

for team in teams:
    url = "https://www.basketball-reference.com/teams/"+team+"/2024.html"
    print(url)
    doc = requests.get(url)
    soup = BeautifulSoup(doc.text, "html.parser")

    body  = soup.find(name = "table", attrs = {"id" : "per_game"}).tbody
    rows = body.find_all(name = "tr")

    dic  =  list()

    for row in rows:
        lst = list()
        stats = row.find_all("td")
        for stat in stats:
            stat = stat.text
            lst.append(stat)
        dic.append(lst)

    data_set  = {"Player": [n[0] for n in dic], "Age" : [n[1] for n in dic], "G":[n[2] for n in dic], "GS" : [n[3] for n in dic],
                  "MP": [n[4] for n in dic], "FG":[n[5] for n in dic], "FGA": [n[6] for n in dic],"FG%":[n[7] for n in dic],
                  "3P":[n[8] for n in dic],"3PA":[n[9] for n in dic],"3P%":[n[10] for n in dic],"2P":[n[11] for n in dic],
                  "2PA":[n[12] for n in dic],"2P%":[n[13] for n in dic],"eFG%":[n[14] for n in dic],"FT":[n[15] for n in dic],
                  "FTA": [n[16] for n in dic],"FT%":[n[17] for n in dic],"ORB":[n[18] for n in dic],"DRB":[n[19] for n in dic],
                  "TRB":[n[20] for n in dic],"AST":[n[21] for n in dic],"STL":[n[22] for n in dic],"BLK":[n[23] for n in dic],
                  "TOV":[n[24] for n in dic],"PF":[n[25] for n in dic],"PTS":[n[26] for n in dic]}

    df = pd.DataFrame(data_set)
    os.makedirs(f".\\final prog\\{team}")
    df.to_csv(f".\\final prog\\{team}\\{team}_table.csv")
    Data_Frames.append(df)
    time.sleep(10)

merged_df = pd.concat(Data_Frames)

file_path = (".\\table.csv")
merged_df.to_csv(file_path)

