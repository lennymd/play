import os
import glob
import pandas as pd

os.chdir("/Users/l.martinez/dev/play/basketball/gamedays")

file_extension = '.csv'
all_filenames = [i for i in glob.glob(f"*{file_extension}")]

combined_csv_data = pd.concat([pd.read_csv(f, delimiter=',', encoding='UTF-8') for f in all_filenames])

os.chdir('..')
combined_csv_data.to_csv('combined_csv_data.csv', index_label = "rows")