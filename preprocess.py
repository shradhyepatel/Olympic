import pandas as pd
import numpy as np

def initialize():
    # Reading the files
    df = pd.read_csv('athlete_events.csv')
    noc = pd.read_csv('noc_regions.csv')

    # Merging both files on the NOC column
    df = df.merge(noc, on="NOC")

    # Dropping Duplicates
    df = df.drop_duplicates()  

    # Adding dummy columns for medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)

    return df
