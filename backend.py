import numpy as np 
import pandas as pd 


def medals(medal_tally):

    medal_tally = medal_tally.drop_duplicates(['Team' , 	'NOC', 	'Games',	'Year',	'Season',	'City',	'Sport'	,'Event' ,	'Medal'])

    medal_tally = medal_tally.groupby('region').sum()[['Gold', 'Silver' , 'Bronze']].sort_values('Gold' , ascending = False ).reset_index()

    medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']

    return medal_tally

def country_list(df):

    country = np.unique(df['region'].dropna()).tolist()
    country.sort()
    country.insert(0 , 'Overall')

    year = np.unique(df['Year'].dropna()).tolist()
    year.sort()
    year.insert(0,'Overall')

    return country , year

def sport_analysis(df):
    sport = df['Sport'].dropna().unique().tolist()
    sport.sort()
    sport.insert(0,'Overall')

    country = np.unique(df['region'].dropna()).tolist()
    country.sort()
    country.insert(0 , 'Overall')

    year = np.unique(df['Year'].dropna()).tolist()
    year.sort()
    year.insert(0,'Overall')

    return sport , country , year

def athlete_analysis(df):
    name = df['Name'].dropna().unique().tolist()
    name.sort()
    name.insert(0,'Overall')

    year = np.unique(df['Year'].dropna()).tolist()
    year.sort()
    year.insert(0,'Overall')

    return name , year

def gender_analysis(df):
    sport = np.unique(df['Sport'].dropna()).tolist()
    sport.sort()
    sport.insert(0,'Overall')

    country = np.unique(df['region'].dropna()).tolist()
    country.sort()
    country.insert(0 , 'Overall')

    return sport , country
    




