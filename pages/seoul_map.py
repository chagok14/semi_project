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
from utils import practice_desc as prac
from utils import map_desc
from streamlit_folium import st_folium

def app():
    
    df = prac.prepare()
    map_desc.map_make()
    
    st.write('''
    아래와 같은 색으로 각 주제분류가 표시되어 있습니다.
    \n
    💚 초록색 : 공연장 \n
    💓 빨간색 : 기타\n
    💗 분홍색 : 도서관\n 
    🧡 주황색 : 문화예술회관 \n  
    💜 보라색 : 문화원 \n
    🖤 검정색 : 미술관 \n
    💙 파란색 : 박물관/기념관
    ''')
    

app()
