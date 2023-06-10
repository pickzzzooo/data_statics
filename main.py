import pandas as pd
import matplotlib as plt
import numpy as np
import time

# 저장 / 스샷 경로
SC_PATH = "C:\\Users\\test2\\Downloads\\data_sicence\\"
DATA_PATH = SC_PATH + "data\\"

# 데이터 딕셔너리
data_dic = pd.read_csv(DATA_PATH + "allranking_data.csv")
allrank_pickrate_dic = {}

for char in data_dic["캐릭터"]:
    if not char in allrank_pickrate_dic: allrank_pickrate_dic[char] = 1
    else: allrank_pickrate_dic[char] += 1

print(allrank_pickrate_dic)


