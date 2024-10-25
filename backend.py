import numpy as np 
import pandas as pd 


def medals(medal_tally):

    #Dropping medals which are repeating for same team
    medal_tally = medal_tally.drop_duplicates(['Team' , 	'NOC', 	'Games',	'Year',	'Season',	'City',	'Sport'	,'Event' ,	'Medal'])

    #Gropuping on region and calculating medals in Decending Order
    medal_tally = medal_tally.groupby('region').sum()[['Gold', 'Silver' , 'Bronze']].sort_values('Gold' , ascending = False ).reset_index()

    #Calculating Total
    medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']

    return medal_tally


