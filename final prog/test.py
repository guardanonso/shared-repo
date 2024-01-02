import pandas as pd
teams = ["SAS","LAL","BOS","CHI"]
for team in teams:
    df = pd.read_csv(f".\\final prog\\{team}\\{team}_table.csv")
    with pd.option_context("display.max_rows", None):
        df = (df.loc[ : , "Player":"PTS"])
    print(f"{df}\n")
