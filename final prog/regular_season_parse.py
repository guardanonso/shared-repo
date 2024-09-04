import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

def csv_creation(start, finish):
    for n in range(start, finish + 1):
        MAIN_URL = f"https://www.basketball-reference.com/leagues/NBA_{n}_per_game.html"

        # parsing main url 
        response = requests.get(MAIN_URL)
        soup = BeautifulSoup(response.text, "html.parser")

        # estraggo le colonne (headers)
        stats_name = soup.find("thead").find_all("th")
        headers = [stat.get("aria-label") for stat in stats_name]

        # Rimuovo primo elemento che non serve
        if headers:
            headers.pop(0)

        rows = soup.find("tbody").find_all("tr")
        lst_of_totals = []

        for row in rows:
            lst = []
            stats = row.find_all("td")
            for stat in stats:
                lst.append(stat.text)
            lst_of_totals.append(lst)

        # creo dataframe
        df = pd.DataFrame(lst_of_totals, columns=headers)
        
        # salvo dataframe convertendolo in file CVS
        df.to_csv(f".\\seasons_stats\\NBAstats_season_{n}.csv", index=False)

        time.sleep(5)

csv_creation(1950, 2024)

