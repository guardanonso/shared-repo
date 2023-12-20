from bs4 import BeautifulSoup
import requests
import pandas as pd
from functools import reduce 

franchises_url = "https://en.wikipedia.org/wiki/Wikipedia:WikiProject_National_Basketball_Association/National_Basketball_Association_team_abbreviations"
document = requests.get(franchises_url)
franchise_soup = BeautifulSoup(document.text, "html.parser")
body = franchise_soup.find("tbody").find_all("tr")
print(body)
for n in body:
    penis = n.find_all()

Data_Frames = []
teams = ["BOS","PHI","LAL","SAS"]
for team in teams:
    url = "https://www.basketball-reference.com/teams/"+team+"/1984.html"
    print(url)
    doc = requests.get(url)
    soup = BeautifulSoup(doc.text, "html.parser")

    # print(soup.prettify)

    body  = soup.find("table", attrs = {"id" : "per_game"}).tbody
    rows = body.find_all(name = "tr")

    dic  =  list()

    for row in rows:
        lst = list()
        stats = row.find_all("td")
        for stat in stats:
            stat = stat.text
            lst.append(stat)
        dic.append(lst)
    
    names_list = [n[0] for n in dic]
    age_list  = [n[1] for n in dic]
    games_played_list = [n[2] for n in dic]
    games_started = [n[3] for n in dic]
    minutes_per_game = [n[4] for n in dic]
    FG = [n[5] for n in dic]
    FGA = [n[6] for n in dic]
    FG_percentage = [n[7] for n in dic]
    threes = [n[8] for n in dic]
    threes_attempts = [n[9] for n in dic]
    threes_percentage = [n[10] for n in dic]
    two_points = [n[11] for n in dic]
    two_points_attempts = [n[12] for n in dic]
    two_points_percentage = [n[13] for n in dic]
    eFG_percentage = [n[14] for n in dic]
    FT = [n[15] for n in dic]
    FTA = [n[16] for n in dic]
    FT_percentage = [n[17] for n in dic]
    ORB = [n[18] for n in dic]
    DRB = [n[19] for n in dic]
    TRB = [n[20] for n in dic]
    AST = [n[21] for n in dic]
    STL = [n[22] for n in dic]
    BLK = [n[23] for n in dic]
    TOV = [n[24] for n in dic]
    PF = [n[25] for n in dic]
    PTS = [n[26] for n in dic]

    data_set  = {"Player": names_list, "Age" : age_list, "G":games_played_list, "GS" : games_started, "MP":minutes_per_game, "FG":FG, "FGA":FGA,"FG%":FG_percentage,"3P":threes,"3PA":threes_attempts,"3P%":threes_percentage,"2P":two_points,"2PA":two_points_percentage, "2P%":two_points_percentage,"eFG%":eFG_percentage,"FT":FT,"FTA": FTA, "FT%":FT_percentage,"ORB":ORB,"DRB":DRB,"TRB":TRB,"AST":AST,"STL":STL,"BLK":BLK,"TOV":TOV,"PF":PF,"PTS":PTS}

    df = pd.DataFrame(data_set)
    Data_Frames.append(df)

merged_df = pd.concat(Data_Frames)

file_path = ("C:\\Users\\RYZEN-GTX-1060\\Desktop\\test_repo\project\\final prog\\ciau.csv")
merged_df.to_csv(file_path)

