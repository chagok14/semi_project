import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import numpy as np
import random 
import folium
import matplotlib.pyplot as plt
import seaborn as sns

from pages import intro
from pages import seoul_map as m
from pages import info
from pages import search

from utils import practice_desc as prac
from utils import intro_desc
from utils import search_desc
from utils import map_desc
from utils import info_desc

st.title('서울 문화시설 정보 확인')

item_list = ['item0','item1', 'item2', 'item3']

item_labels = {'item0':'페이지소개', 'item1':'장소 검색', 'item2':'문화시설 지도', 'item3':'문화시설 정보'}

FIL = lambda x : item_labels[x]
item = st.sidebar.selectbox('가고 싶은 페이지를 선택해 주세요 :)',  item_list, format_func = FIL )
     
if item == 'item0':
	intro.app()
elif item == 'item1':
	search.app()
elif item == 'item2':
        m.app()
   
elif item == 'item3':
        info.app()
elif item == 'item4':
        pr.app()

      
