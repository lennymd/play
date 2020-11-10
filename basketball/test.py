from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType

seasons = [year for year in range(2010,2021)]

for season in seasons:
    years = str(season-1) +"_"+ str(season)
    client.season_schedule(
        season_end_year=season, 
        output_type=OutputType.CSV, 
        output_file_path="./basketball/seasons/"+years+"_season.csv"
    )