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
     

def country_year_selected_analysis(df , country , year):
        
        temp_df = df[(df['region'] == country) & (df['Year'] == year)] 

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

def sport_overall_analysis(df):
        
      
        total_players_participated = df['ID'].drop_duplicates().shape[0]

        total_no_of_games = df['Sport'].drop_duplicates().shape[0]

        no_of_males_females = df.drop_duplicates(['ID'])['Sex'].value_counts()

        no_of_games_over_the_years = df.groupby('Year')['Sport'].nunique().reset_index()
        games = px.bar(no_of_games_over_the_years , x = 'Year' , y = 'Sport')

        players_dif_games = df.drop_duplicates(['ID' , 'Sport']).groupby('Sport')['ID'].nunique().sort_values(ascending = False).reset_index().rename(columns={'ID': 'No Of Players'})

        dff = df.drop_duplicates(['ID' , 'Sport']).groupby(['Sport'])['Sex'].value_counts().reset_index().rename(columns={'count': 'No Of Players'})
        dff = px.bar(dff , x = 'Sport' , y = 'No Of Players' , color= 'Sex')

        return total_players_participated , total_no_of_games , no_of_males_females , games , players_dif_games , dff 

def sport_country_selected_analysis(df , country):
        
        df = df[df['region'] == country]   

        total_players_participated = df['ID'].drop_duplicates().shape[0]

        total_no_of_games = df['Sport'].drop_duplicates().shape[0]

        no_of_males_females = df.drop_duplicates(['ID'])['Sex'].value_counts()

        players_dif_games = df.drop_duplicates(['ID' , 'Sport']).groupby('Sport')['ID'].nunique().sort_values(ascending = False).reset_index().rename(columns={'ID': 'No Of Players'})

        dff = df.drop_duplicates(['ID' , 'Sport']).groupby(['Sport'])['Sex'].value_counts().reset_index()
        dff = px.bar(dff , x = 'Sport' , y = 'count' , color= 'Sex')

        df = df.drop_duplicates(['Team' , 	'NOC', 	'Games',	'Year',	'Season',	'City',	'Sport'	,'Event' ,	'Medal'])
        medal_sport_dristibution = df.groupby('Medal')['Sport'].value_counts().reset_index().rename(columns={'count' : 'Medal Count'})
        medal_sport_dristibutions = px.bar(medal_sport_dristibution , x = 'Sport' , y = 'Medal Count' , color = 'Medal')


        return total_players_participated , total_no_of_games , no_of_males_females , players_dif_games , dff , medal_sport_dristibutions

def sport_year_selected(df , year):
      
      df = df[df['Year'] == year]  

      no_of_playres = df['ID'].drop_duplicates().nunique()

      total_no_of_games = df['Sport'].drop_duplicates().shape[0]

      no_of_males_females = df.drop_duplicates(['ID'])['Sex'].value_counts()

      players_dif_games = df.drop_duplicates(['ID' , 'Sport']).groupby('Sport')['ID'].nunique().sort_values(ascending = False).reset_index().rename(columns={'ID': 'No Of Players'})

      dff = df.drop_duplicates(['ID' , 'Sport']).groupby(['Sport'])['Sex'].value_counts().reset_index()
      dff = px.bar(dff , x = 'Sport' , y = 'count' , color= 'Sex')

      medal = medals(df)

      return no_of_playres , total_no_of_games , no_of_males_females ,players_dif_games , dff , medal 

def sport_selected_only(df , sport):
      
      dff = df[df['Sport'] == sport]

      no_of_players = dff['ID'].drop_duplicates().nunique()

      no_of_males_females = dff.drop_duplicates(['ID'])['Sex'].value_counts()

      no_of_country_participated = dff.drop_duplicates(['ID'])['region'].value_counts().shape[0]

      x = dff.drop_duplicates(['ID'])['region'].value_counts().reset_index().rename(columns = {'count' : 'No Of Players'})
      players_from_diff_country = px.bar( x , x = 'region' , y = 'No Of Players') 

      avg_height = dff.groupby('Sex')['Height'].mean()

      avg_weight = dff.groupby('Sex')['Weight'].mean()

      overall_participation_age = dff.groupby('Sex')['Age'].mean()

      xx = dff.drop_duplicates(['ID'])

      filtered_data = xx[~xx['Medal'].isna()]
      grouped = filtered_data.groupby(['Sex', 'Medal'])
      avg_weight_of_winners = grouped['Weight'].mean()
      avg_height_of_winners = grouped['Height'].mean()
      avg_age_of_winners = grouped['Age'].mean()

      filtered_data = dff.groupby('region')['Medal'].value_counts().reset_index()
      filtered_data = px.bar(filtered_data , x = 'region' , y = 'count' , color='Medal')

      no_of_players_over_the_years = dff.groupby('Year')['ID'].nunique().reset_index().rename(columns = {"ID" : 'Players'})
      no_of_players_over_the_years = px.bar(no_of_players_over_the_years, x = 'Year' , y = 'Players')

      return no_of_players , no_of_males_females , no_of_country_participated , players_from_diff_country , avg_height , avg_weight , overall_participation_age , avg_weight_of_winners ,avg_height_of_winners ,avg_age_of_winners , filtered_data , no_of_players_over_the_years

def sport_and_country_selected(df , sport , country):
      
      temp_df = df[(df['Sport'] == sport) & (df['region'] == country)]

      no_of_unique_players = temp_df['ID'].drop_duplicates().nunique()

      no_of_times_country_participated = temp_df['Year'].nunique()

      no_of_males_females = temp_df.drop_duplicates(['ID'])['Sex'].value_counts()

      graph = temp_df.groupby('Year')['Sex'].value_counts().reset_index()
      graph_males_females_total = px.line(graph , x = 'Year' , y = 'count' , color = 'Sex')

      temp_dff = temp_df.drop_duplicates(['Team' , 	'NOC', 	'Games',	'Year',	'Season',	'City',	'Sport'	,'Event' ,	'Medal'])
      temp = temp_dff.groupby('Medal')['Sex'].value_counts()

      avg_age = temp_df.drop_duplicates('ID').groupby('Sex')['Age'].mean()

      avg_height = temp_df.drop_duplicates('ID').groupby('Sex')['Height'].mean()

      avg_weight = temp_df.drop_duplicates('ID').groupby('Sex')['Weight'].mean()

      
      grouped = temp_df.groupby(['Medal' , 'Sex'])
      avg_weight_of_winners = grouped['Weight'].mean()
      avg_height_of_winners = grouped['Height'].mean()
      avg_age_of_winners = grouped['Age'].mean()

      return no_of_unique_players , no_of_times_country_participated , no_of_males_females , graph_males_females_total , temp , avg_age , avg_height , avg_weight , avg_height_of_winners , avg_weight_of_winners , avg_age_of_winners
         
    




