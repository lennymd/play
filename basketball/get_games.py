from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
from time import sleep
from os import path

days = [day for day in range(1,32)]
months = [month for month in range(1,13)]
years = [year for year in range(2009,2021)]

for a_year in years:
    for a_month in months:
        for a_day in days:
            date = "-".join([str(a_year), str(a_month), str(a_day)])
            file_path = "./game_games/"+date+"_box_scores.csv"
            if path.exists(file_path):
                pass
            else:
                client.team_box_scores(
                    day=a_day, month=a_month, year=a_year, 
                    output_type=OutputType.CSV, 
                    output_file_path=file_path
                )   
                print(date,"done")
                sleep(0.5)