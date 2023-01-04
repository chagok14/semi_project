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
    
    m = folium.Map(
    location = [37.55, 126.98], zoom_start = 12)
    
    marker_cluster = MarkerCluster().add_to(m)
    
    for name, lat, lng, op in zip(df.문화시설명, df.위도, df.경도, df.주제분류_new):
        if op == 0:
            folium.Marker([lat, lng], popup = name, icon = folium.Icon(color = 'green')).add_to(marker_cluster)
        elif op == 1:
            folium.Marker([lat, lng], popup = name, icon = folium.Icon(color = 'red')).add_to(marker_cluster)
        elif op == 2:
            folium.Marker([lat, lng], popup = name, icon = folium.Icon(color = 'pink')).add_to(marker_cluster)
        elif op == 3:
            folium.Marker([lat, lng], popup = name, icon = folium.Icon(color = 'orange')).add_to(marker_cluster)
        elif op == 4:
            folium.Marker([lat, lng], popup = name, icon = folium.Icon(color = 'purple')).add_to(marker_cluster)
        elif op == 5:
            folium.Marker([lat, lng], popup = name, icon = folium.Icon(color = 'black')).add_to(marker_cluster)
        elif op == 6:
            folium.Marker([lat, lng], popup = name, icon = folium.Icon(color = 'blue')).add_to(marker_cluster)

        
    st_data = st_folium(m)
    
    st.write('''
    아래와 같은 색으로 각 주제분류가 표시되어 있습니다.
    \n
    💚 초록색 : 공연장 \n
    ❤ 빨간색 : 기타\n
    💗 분홍색 : 도서관\n 
    🧡 주황색 : 문화예술회관 \n  
    💜 보라색 : 문화원 \n
    🖤 검정색 : 미술관 \n
    💙 파란색 : 박물관/기념관
    ''')
    

app()
