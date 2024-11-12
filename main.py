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

     st.dataframe(responce)

elif opt == 'Country-Wise Analysis':
    country , year = backend.country_list(df)
    st.title('Country Analysis')

    st.sidebar.selectbox('Select a Country' , country)
    st.sidebar.selectbox('Select a Year' , year)

elif opt == 'Sport-Wise Analysis':
    sport , country , year = backend.sport_analysis(df)
    st.title('Sport Analysis')

    st.sidebar.selectbox('Select a Sport' , sport)
    st.sidebar.selectbox('Select a Country' , country)
    st.sidebar.selectbox('Select a Year' , year)

elif opt == 'Gender-Wise Analysis':
    sport , country = backend.gender_analysis(df)
    st.title('Athlete Analysis')

    st.sidebar.selectbox('Select a Gender' , ['Both' , 'Male' , 'Female'])
    st.sidebar.selectbox('Select a Sport' , sport)
    st.sidebar.selectbox('Select a Country' , country)



