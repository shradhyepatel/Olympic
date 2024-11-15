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
    st.subheader(country)

    if country == 'Overall':
        no_of_players , fig , top_10_chart , medals_graph = backend.overall_analysis(df)

        st.text('Total no of players participated each year')
        st.plotly_chart(no_of_players)

        st.text('Total no of Males and Females participated every year')
        st.plotly_chart(fig)

        st.text('Top 10 countries with highest no of Total medals')
        st.plotly_chart(top_10_chart)
        
        st.text('Medal distribution between Male and Female')
        st.plotly_chart(medals_graph)
        


    else:
        responce = backend.country_analysis(country , df)
        st.plotly_chart(responce)

    

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



