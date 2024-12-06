import streamlit as st
import numpy as np 
import pandas as pd 
import plotly.express as xp
import preprocess
import backend 

df = preprocess.initialize()

st.sidebar.title('Olympics Analysis')
opt = st.sidebar.radio('Select An Option' , ['Medal Tally' , 'Country-Wise Analysis' , 'Sport-Wise Analysis' , 'Gender-Wise Analysis'])

if opt == 'Medal Tally':
     st.title('Medal Tally')
     responce = backend.medals(df)

     st.dataframe(responce , use_container_width=True , hide_index= True)

elif opt == 'Country-Wise Analysis':
    country , year = backend.country_list(df)
    st.title('Country-Wise Analysis')

    country = st.sidebar.selectbox('Select a Country' , country)
    year = st.sidebar.selectbox('Select a Year' , year)

    if country == 'Overall' and year == 'Overall':
        no_of_player , fig , top_10_chart , medals_graph = backend.overall_analysis(df)

        st.text('Total no of players participated each year')
        st.plotly_chart(no_of_player)

        st.text('Total no of Males and Females participated every year')
        st.plotly_chart(fig)

        st.text('Top 10 countries with highest no of Total medals')
        st.plotly_chart(top_10_chart)
        
        st.text('Medal distribution between Male and Female')
        st.plotly_chart(medals_graph)
    
    elif country == 'Overall' and year != 'Overall':
        no_of_player , total_country_participated , male_female , tally ,  sport_pie_graph , avg_height , avg_weight = backend.year_selected_analysis(df , year)
        st.subheader(year)
        col1  , col2  , col3= st.columns(3)

        with col1 :
                 st.metric(label="Total no of unique players participated ", value=no_of_player)
        with col2 :
                 st.metric(label="Toatal no of countries participated", value=total_country_participated)
        with col3 :
                 st.write('Total male and female participated')
                 st.dataframe(male_female)

        st.title('Medal tally of year {}'.format(year))
        st.dataframe(tally, use_container_width=True  ,  hide_index= True)

        st.title('Sport contribution in the year {}'.format(year))
        st.plotly_chart(sport_pie_graph)

        col1 , col2 = st.columns(2)

        with col1:
            st.subheader('Avg hight of all participated players')
            st.dataframe(avg_height)

        with col2:
            st.subheader('Avg weight of all participated players')
            st.dataframe(avg_weight)

    elif country != 'Overall' and year == 'Overall':
       
        st.subheader(country)
        each_year , no_of_unique_players , times_country_participated , medal_graph ,sport_participation ,medal_sport_dristibution ,avg_weight ,avg_height , male_female_total = backend.country_selected_analysis(df , country)

        col1 , col2 , col3 = st.columns(3)

        with col1:
            st.metric(label = 'No of unique players participated (Total)' , value = no_of_unique_players)

        with col2:
            st.metric(label = 'No of Times country participated' , value = times_country_participated)

        with col3:
            st.write('Male and Female participation (Total)')
            st.dataframe(male_female_total)

        st.subheader('No of athletes participated each year')
        st.plotly_chart(each_year)

        st.subheader('No of Medal')
        st.plotly_chart(medal_graph)

        st.subheader('{} participation in different sport'.format(country))
        st.plotly_chart(sport_participation)

        st.subheader('Medal from different sport')
        st.plotly_chart(medal_sport_dristibution)

        st.write('Average Height')
        st.dataframe(avg_height)

        st.write('Average Weight')
        st.dataframe(avg_weight)

    elif country != 'Overall' and year != 'Overall':
       
        st.subheader(country)
        this_year , no_of_unique_players , times_country_participated , medal_graph ,sport_participation ,medal_sport_dristibution ,avg_weight ,avg_height , male_female_total = backend.country_year_selected_analysis(df , country , year)

        col1 , col2 , col3 = st.columns(3)

        with col1:
            st.metric(label = 'No of unique players participated (Total)' , value = no_of_unique_players)

        with col2:
            st.metric(label = 'No of Times country participated' , value = times_country_participated)

        with col3:
            st.write('Male and Female participation (Total)')
            st.dataframe(male_female_total)

        st.subheader('No of athletes participated this year')
        st.plotly_chart(this_year)

        st.subheader('No of Medal')
        st.plotly_chart(medal_graph)

        st.subheader('{} participation in different sport'.format(country))
        st.plotly_chart(sport_participation)

        st.subheader('Medal from different sport')
        st.plotly_chart(medal_sport_dristibution)

        st.write('Average Height')
        st.dataframe(avg_height)

        st.write('Average Weight')
        st.dataframe(avg_weight)

elif opt == 'Sport-Wise Analysis':
    sport , country , year = backend.sport_list(df)
    st.title('Sport-Wise Analysis')

    sport = st.sidebar.selectbox('Select a Sport' , sport)
    country = st.sidebar.selectbox('Select a Country' , country)
    year = st.sidebar.selectbox('Select a Year' , year)

    if sport == 'Overall' and country == 'Overall' and year == 'Overall':

     total_players_participated, total_no_of_games, no_of_males_females, games, players_dif_games, dffff = backend.sport_overall_analysis(df)
    
     st.subheader('Overall Sport Analysis')

     col1, col2, col3 = st.columns(3)
     with col1:
            st.metric(label='Total Unique Players Participated till 2016', value=total_players_participated)
        
     with col2:
            st.metric(label='Total Number of Sports', value=total_no_of_games)

     with col3:
            st.write('Male and Female Participation till 2016')
            st.dataframe(no_of_males_females)

     st.subheader('Number of Games Organized Per Year')
     st.plotly_chart(games)

     st.subheader('Number of Players Participated in Each Sport')
     st.dataframe(players_dif_games, use_container_width=True, hide_index=True)

     st.subheader('Male and Female Participation Across Games')
     st.plotly_chart(dffff)

    elif sport == 'Overall' and country != 'Overall' and year == 'Overall':
     
     total_players_participated, total_no_of_games, no_of_males_females, players_dif_games, dfff, medal_sport_distributions = backend.sport_country_selected_analysis(df, country)
    
     st.subheader(f'Overall Sport Analysis of {country}')

     col1, col2, col3 = st.columns(3)

     with col1:
         st.metric(label='Total Unique Players Participated till 2016', value=total_players_participated)

     with col2:
        st.metric(label='Total Number of Sports', value=total_no_of_games)

     with col3:
        st.write('Male and Female Participation till 2016')
        st.dataframe(no_of_males_females)
     
     st.subheader('No of players participated in different sport')
     st.dataframe(players_dif_games, use_container_width=True, hide_index=True)

     st.subheader('No of males and females participated in Sports')
     st.plotly_chart(dfff)

     st.subheader('Medals dristibution betweeen the sports')
     st.plotly_chart(medal_sport_distributions)

    elif sport == "Overall" and country == 'Overall' and year != 'Overall':
     no_of_playres , total_no_of_games , no_of_males_females ,players_dif_games , dff , medal= backend.sport_year_selected(df , year)

     col1 , col2 , col3 = st.columns(3)

     with col1 :
       st.metric(label = 'Total Players' , value= no_of_playres)

     with col2 :
         st.metric(label= 'Total no of sporrts organised' , value= total_no_of_games)

     with col3 :
         st.subheader('Males and Females participated')
         st.dataframe(no_of_males_females)

     st.subheader('Players participation in different games')
     st.dataframe(players_dif_games , use_container_width=True , hide_index=True)

     st.subheader('No of males and females participated in Sports')
     st.plotly_chart(dff)

     st.subheader('Medal Dristbution')
     st.dataframe(medal , hide_index=True)
    
    elif sport == 'Overall' and country != 'Overall' and year != 'Overall':
     each_year , no_of_unique_players , times_country_participated , medal_graph ,sport_participation ,medal_sport_dristibution ,avg_weight ,avg_height , male_female_total = backend.country_year_selected_analysis(df , country , year)
     col1 , col2 , col3 = st.columns(3)

     with col1:
            st.metric(label = 'No of unique players participated (Total)' , value = no_of_unique_players)

     with col2:
            st.metric(label = 'No of Times country participated' , value = times_country_participated)

     with col3:
            st.write('Male and Female participation (Total)')
            st.dataframe(male_female_total)

     st.subheader('No of athletes participated this year')
     st.plotly_chart(each_year)

     st.subheader('No of Medal')
     st.plotly_chart(medal_graph)

     st.subheader('{} participation in different sport'.format(country))
     st.plotly_chart(sport_participation)

     st.subheader('Medal from different sport')
     st.plotly_chart(medal_sport_dristibution)

     st.write('Average Height')
     st.dataframe(avg_height)

     st.write('Average Weight')
     st.dataframe(avg_weight)
 
    elif sport != 'Overall' and country == 'Overall' and year == 'Overall':
         no_of_players , no_of_males_females , no_of_country_participated , players_from_diff_country , avg_height , avg_weight , avg_age , avg_weight_of_winners ,avg_height_of_winners ,avg_age_of_winners , filtered_data , no_of_players_over_the_years = backend.sport_selected_only(df , sport)

         col1 , col2 , col3 = st.columns(3)
         with col1 :
              st.metric(label= 'No of players participated' , value= no_of_players)

         with col2 :
              st.metric(label = 'No of countries participated' , value = no_of_country_participated)

         with col3 :
              st.subheader('No of Males and Females ')
              st.dataframe(no_of_males_females)
         
         st.subheader('Players participated from the countries')
         st.plotly_chart(players_from_diff_country)

         st.subheader('No of players over the years')
         st.plotly_chart(no_of_players_over_the_years)
         
         st.subheader('Winning countries')
         st.plotly_chart(filtered_data)

         st.header('All Players participated Analysis')
         col1 , col2 , col3 = st.columns(3)

         with col1 :
              st.write('Average height of players')
              st.dataframe(avg_height)

         with col2 :
              st.write('Average weight of players')
              st.dataframe(avg_weight)

         with col3 :
              st.write('Average age of the athlete')
              st.dataframe(avg_age)

         st.header('All medal winners analysis')
         col1 , col2 , col3 = st.columns(3)

         with col1 :
              st.write('Average height of players')
              st.dataframe(avg_height_of_winners)

         with col2 :
              st.write('Average weight of players')
              st.dataframe(avg_weight_of_winners)

         with col3 :
              st.write('Average age of the athlete')
              st.dataframe(avg_age_of_winners)

    elif sport != 'Overall' and country != 'Overall' and year == 'Overall':
        no_of_unique_players , no_of_times_country_participated , no_of_males_females , graph_males_females_total , temp_dff , avg_age , avg_height , avg_weight , avg_height_of_winners , avg_weight_of_winners , avg_age_of_winners = backend.sport_and_country_selected(df , sport , country)

        col1 , col2 , col3 = st.columns(3)

        with col1 :
             st.metric(label = 'Total no unique players' , value= no_of_unique_players)
        
        with col2 :
              st.metric(label= 'No of times participated' , value= no_of_times_country_participated)
        
        with col3 :
             st.write('Total males and females participated')
             st.dataframe(no_of_males_females)

        st.subheader('Males & Females participation over the years')
        st.plotly_chart(graph_males_females_total)

        st.subheader('Medal Counts')
        st.dataframe(temp_dff)

        st.header('Analysis of all players participated')

        col1 , col2 , col3 = st.columns(3)

        with col1:
             st.write('Avg age of males & females')
             st.dataframe(avg_age)

        with col2:
             st.write('Avg hight of males and females')
             st.dataframe(avg_height)

        with col3:
             st.write('Average weight of males and females')
             st.dataframe(avg_weight)

        st.header('Analysis of winning players')

        col1 , col2 , col3 = st.columns(3)

        with col1 :
             st.write('Average age of Males and Females')
             st.dataframe(avg_age_of_winners)

        with col2 :
             st.write('Average hight of Males and Females')
             st.dataframe(avg_height_of_winners)

        with col3 :
             st.write('Average weight of Males and Females')
             st.dataframe(avg_weight_of_winners)

    elif sport != 'Overall' and country == 'Overall' and year != 'Overall':

         no_of_unique , no_of_country , no_of_males_females , male_female_graph , avg_age , avg_height , avg_weight , avg_age_medal , avg_height_medal , avg_weight_medal = backend.sport_and_year_selected(df, sport , year )

         col1 , col2 , col3 = st.columns(3)

         with col1 :
              st.metric(label= 'Total players participated' , value= no_of_unique)

         with col2 :
              st.metric(label='Number of countries participated' , value= no_of_country)
        
         with col3 :
              st.write('Total males and females participated')
              st.dataframe(no_of_males_females)

         st.subheader('Males and female participation from different countries')
         st.plotly_chart(male_female_graph)

         st.subheader('Analysis of all players participated')
         col1 , col2 , col3 = st.columns(3)

         with col1 :
              st.write('Average age of athelete')
              st.dataframe(avg_age)

         with col2 :
              st.write('Average hight of athelets')
              st.dataframe(avg_height)
        
         with col3 :
              st.write('Average weight of athelets')
              st.dataframe(avg_height)

         st.subheader('Analysis of medal winners')
         col1 , col2 , col3 = st.columns(3)

         with col1 :
              st.write('Average age of athelete')
              st.dataframe(avg_age_medal)

         with col2 :
              st.write('Average hight of athelets')
              st.dataframe(avg_height_medal)
        
         with col3 :
              st.write('Average weight of athelets')
              st.dataframe(avg_weight_medal)

    else :
         no_of_unique , no_of_males_females , no_of_diff_event , events_dataframe , avg_age , avg_height , avg_weight , avg_age_medal , avg_height_medal , avg_weight_medal , medal_tally = backend.sport_all_selected(df , sport , country , year )

         col1 , col2 , col3 = st.columns(3)

         with col1 :
              st.metric(label= 'Total no of players' , value= no_of_unique)

         with col2 :
              st.metric(label= 'No of different event' , value= no_of_diff_event)

         with col3 :
              st.write('Total males and females participated')
              st.dataframe(no_of_males_females)

         st.subheader('Events')
         st.dataframe(events_dataframe , use_container_width=True , hide_index= True)

         st.header('Analysis of all players')

         col1 , col2 , col3 = st.columns(3)

         with col1:
              st.write('Average age of athelets')
              st.dataframe(avg_age)

         with col2:
              st.write('Agerage height all athelets')
              st.dataframe(avg_height)

         with col3:
              st.write('Average weight of athelets')
              st.dataframe(avg_weight)

         st.header('Analysis of medal winners')

         col1 , col2 , col3 = st.columns(3)

         with col1:
              st.write('Average age of athelets')
              st.dataframe(avg_age_medal)

         with col2:
              st.write('Agerage height all athelets')
              st.dataframe(avg_height_medal)

         with col3:
              st.write('Average weight of athelets')
              st.dataframe(avg_weight_medal)

         st.header('Medal Tally')
         st.dataframe(medal_tally)


elif opt == 'Gender-Wise Analysis':
     sport , country = backend.gender_list(df)
     st.title('Gender-Wise Analysis')

     gender = st.sidebar.selectbox('Select a Gender' , ['Both' , 'Male' , 'Female'])
     sport = st.sidebar.selectbox('Select a Sport' , sport)
     country = st.sidebar.selectbox('Select a Country' , country)


     if gender == 'Both' and sport == 'Overall'  and country == 'Overall' :
       
       no_of_total_playrs , total_country_participated , males_and_females ,males_females_year_by_year_graph , players_sport_dristribution ,graph_over_the_years , avg_age , avg_height , avg_weight , medal_avg_age , medal_avg_height , medal_avg_weight = backend.gender_overall_analysis(df)

       col1 , col2 , col3 = st.columns(3)

       with col1:
            st.metric(label='Total players participated' , value=no_of_total_playrs)
     
       with col2 :
            st.metric(label='Total countries participated' , value= total_country_participated)

       with col3:
            st.write('No of males and females participated')
            st.dataframe(males_and_females)

       st.subheader('Males and Females year by year (Summer)')
       st.plotly_chart(males_females_year_by_year_graph)

       st.subheader('Players sport distribution')
       st.plotly_chart(players_sport_dristribution)

       st.subheader('No of players from all the participated countries')
       st.plotly_chart(graph_over_the_years)

       st.subheader('Analysis of all players')
       col1 , col2 , col3 = st.columns(3)

       with col1 :
            st.write('Average age of both genders')
            st.dataframe(avg_age)

       with col2 :
            st.write('Avgerage hight of both genders')
            st.dataframe(avg_height)

       with col3 :
            st.write('Average weight of both genders')
            st.dataframe(avg_weight)

       st.subheader('Analysis of medal winners')
       col1 , col2 , col3 = st.columns(3)

       with col1 :
            st.write('Average age of both genders')
            st.dataframe(medal_avg_age)

       with col2 :
            st.write('Avgerage hight of both genders')
            st.dataframe(medal_avg_height)

       with col3 :
            st.write('Average weight of both genders')
            st.dataframe(medal_avg_weight)


     elif gender == 'Both' and sport == 'Overall'  and  country != 'Overall':

          total_players , total_games , males_females_count , every_year_graph_summer , every_year_graph_winter , avg_age ,  avg_height , avg_weight , medal_avg_age , medal_avg_height , medal_avg_weight = backend.gender_country_selected(df , country)
          option = backend.sport_list_in(df , country)

          col1 , col2 , col3 = st.columns(3)

          with col1 :
               st.metric(label= 'Total players participated' , value= total_players)

          with col2 :
               st.metric(label='Total Games Played' , value= total_games)

          with col3:
               st.write('Total males and females')
               st.dataframe(males_females_count)

          st.subheader('Males and females participation (Summer)')
          st.plotly_chart(every_year_graph_summer)

          st.subheader('Males and females participation (Winter)')
          st.plotly_chart(every_year_graph_winter)

          col1 , col2 , col3 = st.columns(3)

          with col1:
            responce = st.selectbox( 'Select a sport' , option)

          graph = backend.sport_graph_in(df ,country , responce)

          st.plotly_chart(graph)

          st.subheader('Analysis of all players')

          col1 , col2 , col3 = st.columns(3)

          with col1 :
               st.write('Average age')
               st.dataframe(avg_age)

          with col2 :
               st.write('Average height')
               st.dataframe(avg_height)

          with col3 :
               st.write('Average weight')
               st.dataframe(avg_weight)

          st.subheader('Analysis of medal winners')

          col1 , col2 , col3 = st.columns(3)

          with col1 :
               st.write('Average age')
               st.dataframe(medal_avg_age)

          with col2 :
               st.write('Average height')
               st.dataframe(medal_avg_height)

          with col3 :
               st.write('Average weight')
               st.dataframe(medal_avg_weight)

     elif gender == 'Both' and country == 'Overall' and sport != 'Overall':

          total_players_unique , total_countries , total_males_females , year_by_year_graph_summer , year_by_year_graph_winter , country_participation_graph , pie_graph , avg_age , avg_height , avg_weight , medal_avg_age , medal_avg_height , medal_avg_weight = backend.gender_sport_selected(df , sport)

          col1 , col2 , col3 = st.columns(3)

          with col1 :
               st.metric(label= 'Total players participated' , value= total_players_unique)

          with col2 :
               st.metric(label = 'Total countries participated' , value= total_countries)

          with col3 :
               st.write('Total males and females participated')
               st.dataframe(total_males_females)

          st.subheader('Males and females participation (Summer)')
          st.plotly_chart(year_by_year_graph_summer)

          st.subheader('Males and females participation (Winter)')
          st.plotly_chart(year_by_year_graph_winter)

          st.subheader('Countries participation over the years')
          st.plotly_chart(country_participation_graph)

          st.subheader('Top 30 countries')
          st.plotly_chart(pie_graph)

          st.subheader('Analysis of all players participated')
          
          col1 , col2 , col3 = st.columns(3)

          with col1 :
               st.write('Average age')
               st.dataframe(avg_age)
          
          with col2 :
               st.write('Average height')
               st.dataframe(avg_height)

          with col3 :
               st.write('Average weight')
               st.dataframe(avg_weight)

          st.subheader('Analysis of medal winners')
          
          col1 , col2 , col3 = st.columns(3)

          with col1 :
               st.write('Average age')
               st.dataframe(medal_avg_age)
          
          with col2 :
               st.write('Average height')
               st.dataframe(medal_avg_height)

          with col3 :
               st.write('Average weight')
               st.dataframe(medal_avg_weight)               
                               
                 
                 

          


           



      
            



