import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import numpy as np
import random 
import folium
import matplotlib.pyplot as plt
import seaborn as sns
from utils import info_desc 
from utils import practice_desc as prac

def app():
    info_desc.showSubGraph()    
    info_desc.showGraph()

app()


