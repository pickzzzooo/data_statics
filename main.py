import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import time, glob, json

# 내꺼
import allrank_pickrate as all_pr
import specrank_pickrate as sr_pr
import graph_manager as grh_m
import tier_maker as t_m

# 저장 / 스샷 경로
SC_PATH = "C:\\Users\\test2\\Downloads\\data_sicence\\"     # 최상위 디렉토리.
DATA_PATH = SC_PATH + "data\\"
CHAR_DATA_PATH = DATA_PATH + "char_data\\*"
ALLRANK_DATA_PATH = DATA_PATH + "allranking_data.csv"


# 폰트 설정 / json
FONT_PATH = SC_PATH + "fonts\\NanumGothic.ttf"
FONT_PROP = font_manager.FontProperties(fname=FONT_PATH).get_name()
rc("font", family=FONT_PROP)




# 전체 랭킹 캐릭터 유저수
pr_key_arr = ["캐릭터", "유저 수", "상위 1만명 각 캐릭터의 유저 비율"]
#all_pr.create_table(ALLRANK_DATA_PATH, pr_key_arr)    #표
#all_pr.create_pie(ALLRANK_DATA_PATH, pr_key_arr)       #원그래프
#all_pr.create_barh(ALLRANK_DATA_PATH, pr_key_arr)      #막대 그래프
#all_pr.create_wc(ALLRANK_DATA_PATH, FONT_PATH, pr_key_arr)   #워드 클라우드


# 계급 분포도
rr_key_arr = ["계급", "비율", "상위 1만명 계급 분포율"]
#all_pr.create_table(ALLRANK_DATA_PATH, rr_key_arr) #표
#all_pr.create_pie(ALLRANK_DATA_PATH, rr_key_arr)   #원그래프
#all_pr.create_barh(ALLRANK_DATA_PATH, rr_key_arr)   #막대 그래프
#all_pr.create_wc(ALLRANK_DATA_PATH, FONT_PATH, rr_key_arr)   #워드 클라우드

# 특정 계급속 캐릭터 유저 수
RANK = "마이티 룰러"
sr_key_arr = ["계급", "비율", RANK + " 캐릭터 분포도"]
#sr_pr.create_table(RANK, glob.glob(CHAR_DATA_PATH), DATA_PATH, sr_key_arr)    #표
#sr_pr.create_pie(RANK, glob.glob(CHAR_DATA_PATH), DATA_PATH, sr_key_arr)     #원그래프
#sr_pr.create_barh(RANK, glob.glob(CHAR_DATA_PATH), DATA_PATH, sr_key_arr)     #막대 그래프
#sr_pr.create_wc(RANK, glob.glob(CHAR_DATA_PATH), DATA_PATH, sr_key_arr, FONT_PATH)    #워드클라우드



# 메타 포인트
data = t_m.meta_point_cal(glob.glob(CHAR_DATA_PATH))
data = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
meta_key_arr = ["계급", "메타 포인트", "캐릭터별 메타포인트"]

t_m.create_table(data, meta_key_arr)    #표
grh_m.create_brah(data, meta_key_arr)   #막대 그래프
grh_m.create_wc(data, FONT_PATH, meta_key_arr) # 워드 클라우드

