import os
import glob
import pandas as pd
import csv
os.chdir("/Users/l.martinez/dev/play/basketball/game_files")

file_extension = '.csv'
all_filenames = [i for i in glob.glob(f"*{file_extension}")]

games = []
header = ['team', 'minutes_played', 'made_field_goals', 'attempted_field_goals', 'made_three_point_field_goals', 'attempted_three_point_field_goals', 'made_free_throws', 'attempted_free_throws', 'offensive_rebounds', 'defensive_rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'personal_fouls', 'points', 'outcome','year','month','day','date']
games.append(header)

for a in all_filenames:
    # read file into a list
    with open(a) as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    if (len(rows) == 1):
        pass
        # no data for that day
    else:
        date_long = a.split("_")[0]
        date = date_long.split("-")
        # read row and append
        for row in rows[1:]:
            temp_row = row
            for item in date:
                temp_row.append(item)
            temp_row.append(date_long)
            games.append(temp_row)
    
with open("../game_data_all.csv", mode="w") as f:
    w = csv.writer(f,delimiter=",", quoting=csv.QUOTE_MINIMAL)
    w.writerows(games)



