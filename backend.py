import numpy as np 
import pandas as pd 
import plotly.express as px

def unique(df):
     
     df = df.drop_duplicates(['Team' , 	'NOC', 	'Games',	'Year',	'Season',	'City',	'Sport'	,'Event' ,	'Medal'])

     return df

def medals(df):

    medal_tally = unique(df)
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

def sport_list(df):
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

def athlete_list(df):
    name = df['Name'].dropna().unique().tolist()
    name.sort()
    name.insert(0,'Overall')

    year = np.unique(df['Year'].dropna()).tolist()
    year.sort()
    year.insert(0,'Overall')

    return name , year

def gender_list(df):
    sport = np.unique(df['Sport'].dropna()).tolist()
    sport.sort()
    sport.insert(0,'Overall')

    country = np.unique(df['region'].dropna()).tolist()
    country.sort()
    country.insert(0 , 'Overall')

    return sport , country

def country_analysis(country , df):
        temp_df = df[df['region'] == country]
        graph = temp_df['Year'].value_counts()
        no_of_players = px.bar(graph)
        no_of_players.update_layout(
                            xaxis_title="Year",
                            yaxis_title="No of Players")
        
        return no_of_players

def overall_analysis(df):
        
        #df = unique(df)

        graph = df['Year'].value_counts()
        no_of_players = px.bar(graph)
        no_of_players.update_layout(
                            xaxis_title="Year",
                            yaxis_title="No of Players")
        
        fig = px.histogram(df  , x = 'Year' ,  color = 'Sex')
        fig.update_layout(
                  xaxis_title="Year",
                  yaxis_title="No of Players")
        
        meda_tally = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
        meda_tally = meda_tally.drop_duplicates(['Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'])
        meda_tally = meda_tally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']]
        meda_tally['Total'] = meda_tally[['Gold', 'Silver', 'Bronze']].sum(axis=1)/2
        meda_tally = meda_tally.drop(['Gold', 'Silver', 'Bronze'], axis=1).sort_values(by='Total', ascending=False).reset_index()
        top_10 = meda_tally.head(10)
        top_10_chart = px.bar(top_10, x='region', y='Total', color='region')

        top_10_chart.update_layout(
            xaxis_title="Region", 
            yaxis_title="Total Medals" 
        )

        medals_graph= px.histogram(df , x = 'Medal' , color = 'Sex')
        medals_graph.update_layout(
            xaxis_title="Medals", 
            yaxis_title="Total Medals" 
        )
        
        return no_of_players , fig , top_10_chart , medals_graph

def year_selected_analysis(df , year):
        
        temp_df = df[df['Year'] == year]
        temp_df.drop_duplicates(inplace= True)

        no_of_player = temp_df['ID'].drop_duplicates().value_counts().sum()

        total_country_participated = temp_df['region'].drop_duplicates().value_counts().sum()

        male_female = temp_df['Sex'].value_counts()

        medal_tally = unique(temp_df)
        medal_tally = medal_tally.groupby('region').sum()[['Gold', 'Silver' , 'Bronze']].sort_values('Gold' , ascending = False ).reset_index()
        medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']

        sport_dristibution = temp_df['Sport'].value_counts().reset_index()
        sport_pie = px.pie(sport_dristibution , names = 'Sport' , values = 'count')
        
        avg = unique(temp_df)

        avg_height = avg.groupby('Sex')['Height'].mean()

        avg_weight = avg.groupby('Sex')['Weight'].mean()

        return no_of_player , total_country_participated , male_female , medal_tally ,  sport_pie , avg_height , avg_weight

def country_selected_analysis(df , country):
        
        temp_df = df[df['region'] == country]

        no_of_athelete_each_year = temp_df['Year'].value_counts().drop_duplicates().reset_index()
        each_year = px.bar(no_of_athelete_each_year , x = 'Year' , y = 'count')

        no_of_unique_players = temp_df['ID'].value_counts().shape[0]

        times_country_participated = temp_df['Year'].value_counts().drop_duplicates().reset_index().shape[0]
    
        temp_dff = temp_df.drop_duplicates(['Team' , 	'NOC', 	'Games',	'Year',	'Season',	'City',	'Sport'	,'Event' ,	'Medal'])
        medal_graph = temp_dff['Medal'].value_counts().reset_index()
        medal_graph = px.bar(medal_graph , x = 'Medal' , y = 'count' , color = 'Medal')
        
        sport_participation = temp_df['Sport'].value_counts().reset_index()
        sport_participation = px.pie(sport_participation , names = 'Sport' , values = 'count')

        medal_sport_dristibution = temp_df.groupby('Medal')['Sport'].value_counts().reset_index()
        medal_sport_dristibution = px.bar(medal_sport_dristibution , x = 'Sport' , y = 'count' , color = 'Medal')

        temp = unique(temp_df)

        avg_weight = temp.groupby('Sex')['Weight'].mean()

        avg_height = temp.groupby('Sex')['Height'].mean()

        male_female_total = temp['Sex'].value_counts()

        return each_year , no_of_unique_players , times_country_participated , medal_graph ,sport_participation ,medal_sport_dristibution ,avg_weight ,avg_height , male_female_total 
     





    




