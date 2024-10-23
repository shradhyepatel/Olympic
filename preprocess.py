import pandas as pd
import numpy as np

def initialize():

    #Reading the files
    df = pd.read_csv('athlete_events.csv')
    noc = pd.read_csv('noc_regions.csv')

    #Merging both file on NOC column
    df.merge(noc , on = "NOC")

    #Dropping Duplicates
    df.drop_duplicates(inplace = True)

    return df