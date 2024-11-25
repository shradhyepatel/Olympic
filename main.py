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
        pass
    

elif opt == 'Sport-Wise Analysis':
    sport , country , year = backend.sport_list(df)
    st.title('Sport-Wise Analysis')

    st.sidebar.selectbox('Select a Sport' , sport)
    st.sidebar.selectbox('Select a Country' , country)
    st.sidebar.selectbox('Select a Year' , year)

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



