import streamlit as st
import numpy as np 
import pandas as pd 
import preprocess

df = preprocess.initialize()

st.title('Olympic Anaylasis')

st.sidebar.title('Olympics Analysis')
opt = st.sidebar.selectbox('Select An Option' , ['Overall Analysis' , 'General Trends'])

if opt:
    if opt == 'Overall Analysis':
        st.text(opt)
    else :
        st.text(opt)


