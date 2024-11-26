import streamlit as st
import numpy as np 
import pandas as pd 
import plotly.express as xp
import preprocess
import backend 

df = preprocess.initialize()

st.sidebar.title('Olympics Analysis')
opt = st.sidebar.radio('Select An Option' , ['Medal Tally' , 'Country-Wise Analysis' , 'Sport-Wise Analysis' , 'Athlete-Wise Analysis' , 'Gender-Wise Analysis'])

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

     total_players_participated, total_no_of_games, no_of_males_females, games, players_dif_games, dff = backend.sport_overall_analysis(df)
    
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
     st.plotly_chart(dff)

    elif sport == 'Overall' and country != 'Overall' and year == 'Overall':
     
     total_players_participated, total_no_of_games, no_of_males_females, players_dif_games, dff, medal_sport_distributions = backend.sport_country_selected_analysis(df, country)
    
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
     st.plotly_chart(dff)

     st.subheader('Medals dristibution betweeen the sports')
     st.plotly_chart(medal_sport_distributions)

         




elif opt == 'Athlete-Wise Analysis':
    name, year = backend.athlete_list(df)
    st.title('Athlete-Wise Analysis')

    st.sidebar.selectbox('Select a Sport' , name)
    st.sidebar.selectbox('Select a Year' , year)

elif opt == 'Gender-Wise Analysis':
    sport , country = backend.gender_list(df)
    st.title('Gender-Wise Analysis')

    st.sidebar.selectbox('Select a Gender' , ['Both' , 'Male' , 'Female'])
    st.sidebar.selectbox('Select a Sport' , sport)
    st.sidebar.selectbox('Select a Country' , country)



