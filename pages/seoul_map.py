'''
from streamlit_folium import st_folium
import pandas as pd
import numpy as np
import random
import folium
import matplotlib.pyplot as plt
import seaborn as sns
from folium.plugins import MarkerCluster

from utils import info_desc
'''
import streamlit as st
from utils import practice_desc as prac
from utils import map_desc

def app():
    
    df = prac.prepare()
    map_desc.map_make()
    st.write('''
    아래와 같은 색으로 각 주제분류가 표시되어 있습니다.
    \n
    초록색 : 공연장 
    빨간색 : 기타
    분홍색 : 도서관 
    주황색 : 문화예술회관   
    보라색 : 문화원 
    검정색 : 미술관 
    파란색 : 박물관/기념관
    ''')
    

app()
