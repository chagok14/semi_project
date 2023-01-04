import streamlit as st
from utils import practice_desc as prac

def search_func():
    df = prac.prepare()
    df2 = prac.prepare2()

    
    st.write('''
            ### 원하는 문화시설 장소를 보기 위해 옵션을 클릭해 보세요!
            ''')
    st.write('\n')

    sidebar_radio = st.radio("원하는 분류 기준을 선택해 주세요.", ["주제분류", "지역구", "무료구분"])

    subject = ['기타', '공연장', '도서관', '문화예술회관', '미술관', '박물관/기념관', '문화원']
    region = df.구명.unique()
    price = df.무료구분.unique()
    st.write('\n')


    if sidebar_radio == '주제분류':
            selected_subject = st.selectbox('주제를 선택해 주세요.', subject)
            for k in subject:
                    if selected_subject == k:
                            st.write(df2[df2['주제분류'] == k])
                            
    elif sidebar_radio == '지역구':
            selected_gu = st.selectbox('지역구를 선택해 주세요.', region)
            for g in region:
                    if selected_gu == g:
                            st.write(df2[df2['구명'] == g])


    elif sidebar_radio == '무료구분':
            selected_price = st.selectbox('무료구분을 선택해 주세요.', price)
            for p in price:
                    if selected_price == p:
                            st.write(df2[df2['무료구분'] == p])

    
