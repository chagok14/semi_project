    
def prepare():
    
    import streamlit as st
    from streamlit_folium import st_folium
    import pandas as pd
    import numpy as np
    import random
    import matplotlib.pyplot as plt
    import seaborn as sns

    df = pd.read_csv('C:\\Users\\heeji\\Documents\\project_seven\\data\\seoulSpace.csv', encoding = 'euc-kr')
    df.drop(columns = ['번호',  '관람시간', '관람료', '기타사항', '시설소개', '지하철', '버스정거장', 'YELLOW', 'GREEN', 'RED', 'BLUE', '공항버스', '팩스번호', '개관일자', '객석수', '휴관일'], inplace = True)

    df['주소'][df.index == 285] = '서울 송파구 올림픽로 300 롯데월드몰 8층 롯데콘서트홀'
    df['주소'][df.index == 286] = '서울 용산구 백범로 329'

    df['위도'][df.index == 514] = 37.394776199999555
    df['경도'][df.index == 514] = 127.10697565393801

    df['전화번호'].fillna('정보 없음', inplace = True)
    df['홈페이지'].fillna('정보 없음', inplace = True)
    df['무료구분'].fillna('정보 없음', inplace = True)

    import sklearn
    from sklearn.preprocessing import LabelEncoder
    encoder = LabelEncoder()

    df['주제분류_new'] = encoder.fit_transform(df['주제분류'])

    address = df.주소
    add = address.to_list()

    add = pd.Series(add)
    add_new = add.str.split()


    add_list = []
    for i in range(0, len(df.index)):
        add_list.append(add_new[i][1])

    df['구명'] = add_list

    df.구명[df.index == 12] = '종로구'
    df.구명[df.index == 19] = '용산구'
    df.구명[df.index == 329] = '중랑구'
    df.구명[df.index == 345] = '광진구'
    df.구명[df.index == 391] = '강동구'
    df.구명[df.index == 448] = '강남구'
    df.구명[df.index == 452] = '구로구'
    df.구명[df.index == 457] = '동대문구'

    df = df.drop(326)
    df.reset_index(drop = True, inplace = True)

    return df

def prepare2():
    df = prepare()
    df2 = df.copy()
    df2.drop(columns = ['위도', '경도', '대표이미지', '주제분류_new'], inplace = True)

    return df2


