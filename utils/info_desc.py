import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import numpy as np
import random 
import folium
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px

from utils import practice_desc as prac

def showGraph():
    df = prac.prepare()
    plt.rcParams['axes.unicode_minus'] = False
    count_result = df['구명'].value_counts()
    df_sorted = df.sort_values(count_result, ascending = False)
    fig = plotly.bar(df_sorted, x = '지역구', y = 'Count')
    st.plotly_chart(fig)
    '''
    plt.figure(figsize=(12, 30))
    sns.countplot(y=df['구명'], order=df['구명'].value_counts().index)
    plt.yticks(fontsize = 12)
    plt.title('구별 문화공간 개수', size = 18)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    '''

def showSubGraph():
    df = prac.prepare()
    plt.rcParams['axes.unicode_minus'] = False
    fig1 = px.pie(df, values = df.주제분류.value_counts(), names = df.주제분류.unique())
    st.markdown("<h5 style='text-align: center; color: black;'>주제분류별 문화시설 개수</h5>", unsafe_allow_html=True)
    st.plotly_chart(fig1)


    

    
