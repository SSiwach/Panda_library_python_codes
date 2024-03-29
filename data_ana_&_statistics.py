# -*- coding: utf-8 -*-
"""panda_library.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QZz5qj-cFCjoxto8cfwzF_P6k-6hPGVW
"""

import pandas as pd
df = pd.DataFrame(
    {
        "Name" : [
                  "Braund, Mr. Owen Harris",
                  "Allen, Mr. William Henry",
                  "Bonnel, Miss. Elizabeth",

        ],
     "Age":[22,35,58],
     "Sex":["male","male","female"],
    }
)
df

df["Age"]

# create a series from scratch

ages = pd.Series([22,35,58],name = "Age")

ages

#to find Max of the data

df["Age"].max()

# to find max of the data
ages.max()

#basic statistics of numerical data

df.describe()


