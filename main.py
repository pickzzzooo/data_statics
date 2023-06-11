import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import time, glob

# 내꺼
import allrank_pickrate, specrank_pickrate

# 저장 / 스샷 경로
SC_PATH = "C:\\Users\\test2\\Downloads\\data_sicence\\"     # 최상위 디렉토리.
DATA_PATH = SC_PATH + "data\\"
CHAR_DATA_PATH = DATA_PATH + "char_data\\*"
ALLRANK_DATA_PATH = DATA_PATH + "allranking_data.csv"


# 폰트 설정
FONT_PATH = SC_PATH + "fonts\\NanumGothic.ttf"
FONT_PROP = font_manager.FontProperties(fname=FONT_PATH).get_name()
rc("font", family=FONT_PROP)


# 전체 랭킹 캐릭터 유저수
pickrate_key_arr = ["캐릭터", "유저 수", "상위 1만명 각 캐릭터의 유저 비율"]
#allrank_pickrate.create_table(ALLRANK_DATA_PATH, pickrate_key_arr)    #표
#allrank_pickrate.create_pie(ALLRANK_DATA_PATH, pickrate_key_arr)       #원그래프
#allrank_pickrate.create_barh(ALLRANK_DATA_PATH, pickrate_key_arr)      #막대 그래프
#allrank_pickrate.create_wc(ALLRANK_DATA_PATH, FONT_PATH, pickrate_key_arr)   #워드 클라우드


# 계급 분포도
rankrate_key_arr = ["계급", "비율", "상위 1만명 계급 분포율"]
#allrank_pickrate.create_table(ALLRANK_DATA_PATH, rankrate_key_arr) #표
#allrank_pickrate.create_pie(ALLRANK_DATA_PATH, rankrate_key_arr)   #원그래프
#allrank_pickrate.create_barh(ALLRANK_DATA_PATH, rankrate_key_arr)   #막대 그래프
allrank_pickrate.create_wc(ALLRANK_DATA_PATH, FONT_PATH, rankrate_key_arr)   #워드 클라우드

# 특정 계급속 캐릭터 유저 수
RANK = "마이티 룰러"
specrank_key_arr = ["계급", "비율", RANK + " 캐릭터 분포도"]
#specrank_pickrate.create_table(RANK, glob.glob(CHAR_DATA_PATH), DATA_PATH, specrank_key_arr)    #표
#specrank_pickrate.create_pie(RANK, glob.glob(CHAR_DATA_PATH), DATA_PATH, specrank_key_arr)     #원그래프
#specrank_pickrate.create_barh(RANK, glob.glob(CHAR_DATA_PATH), DATA_PATH, specrank_key_arr)     #막대 그래프
#specrank_pickrate.create_wc(RANK, glob.glob(CHAR_DATA_PATH), DATA_PATH, specrank_key_arr, FONT_PATH)    #워드클라우드

# 티어

