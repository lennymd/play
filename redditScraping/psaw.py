#!/usr/bin/env python
# coding: utf-8

import datetime as dt
import pandas as pd
from psaw import PushshiftAPI

api = PushshiftAPI()

df = pd.DataFrame(
    list(
        api.search_submissions(
            subreddit="COVID19_support",
            filter=["title", "url", "selftext", "score"],
            limit=60000,
        )
    )
)

# df["created_utc"] = pd.to_datetime(df["created_utc"], unit="s").dt.date


print(df.head())
print(len(df))


# df.to_csv("dataset_1006.csv")

