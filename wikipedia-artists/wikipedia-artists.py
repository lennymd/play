import wikipediaapi
import string
import csv
import time

# After a short test, I want to get the artists and their summaries and save that information to a CSV File with the columns: "artist_name", "summary", "url"

wiki = wikipediaapi.Wikipedia("Lenny Test Project (lennymartinezd@gmail.com)", "en")
# TEST_PAGE = "Vincent_van_Gogh"

## PART 1 -- Get all the painters we'll use
# painter_list = ["name"]
# alphabet = list(string.ascii_uppercase)
# for letter in alphabet:
#     page = wiki.page(f'List_of_painters_by_name_beginning_with_"{letter}"')
#     if page.exists():
#         print(f"Page - {page.title}")
#         for link in page.links:
#             painter_list.append(link.replace(" ", "_"))

# Save painter_list to a CSV file
# with open("./wikipedia-artists/painter_list_raw.csv", mode="w", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     for painter in painter_list:
#         writer.writerow([painter])

# PART 1.5 -- read the painter list from the CSV file
print("Loading all artists")
painter_list = []
with open(
    "./wikipedia-artists/painter_list_cleaned.csv", mode="r", encoding="utf-8"
) as file:
    reader = csv.reader(file)
    for row in reader:
        painter_list.append(row[0])
print("\nLoaded all artists")
print("------------------")

# PART 2 -- Get the summaries of the painters
print("Getting data for artists")
painter_data = [["wikipedia_name", "artist_name", "summary", "url"]]
for painter in painter_list[3700:]:
    page = wiki.page(painter)
    _index = painter_list.index(painter)
    if page.exists():
        print(f"Looking at number {_index+1}: {page.title}")
        painter_data.append([painter, page.title, page.summary, page.fullurl])

    if _index % 100 == 0:
        time.sleep(2)
    #     with open(f"./painter_data_{_index}.csv", mode="w", encoding="utf-8") as file:
    #         writer = csv.writer(file)
    #         for painter in painter_data:
    #             writer.writerow(painter)
    #     print(f"Saved data to CSV file up to {_index}/{len(painter_list)-1}")
    #     time.sleep(4)

with open(f"./painter_data_end.csv", mode="w", encoding="utf-8") as file:
    writer = csv.writer(file)
    for painter in painter_data:
        writer.writerow(painter)
    print(f"Saved data to CSV file up to {_index}/{len(painter_list)-1}")
    time.sleep(4)
