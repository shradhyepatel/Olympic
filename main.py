import streamlit as st
import numpy as np 
import pandas as pd 
import plotly.express as xp
import preprocess
import backend 

df = preprocess.initialize()

st.title('Olympic Anaylasis')

st.sidebar.title('Olympics Analysis')
opt = st.sidebar.radio('Select An Option' , ['Medal Tally' , 'General Trends'])

if opt:
    if opt == 'Medal Tally':
        responce = backend.medals(df)
        st.dataframe(responce)
    else :
        st.text(opt)


