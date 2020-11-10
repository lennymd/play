from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType

days = [day for day in range(1,32)]
months = [month for month in range(1,13)]
years = [year for year in range(2009,2021)]

for a_year in years:
    for a_month in months:
        for a_day in days:
            date = "-".join([str(a_year), str(a_month), str(a_day)])
            print(date)
            client.team_box_scores(
                day=a_day, month=a_month, year=a_year, 
                output_type=OutputType.CSV, 
                output_file_path="./basketball/gamedays/"+date+"_box_scores.csv"
            )

# Get all season game days & scores
# for season in seasons:
#     years = str(season-1) +"_"+ str(season)
#     client.season_schedule(
#         season_end_year=season, 
#         output_type=OutputType.CSV, 
#         output_file_path="./basketball/seasons/"+years+"_season.csv"
#     )

