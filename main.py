import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import time

# 내꺼
import allrank_pickrate

# 저장 / 스샷 경로
SC_PATH = "C:\\Users\\test2\\Downloads\\data_sicence\\"     # 최상위 디렉토리.
DATA_PATH = SC_PATH + "data\\"

# 폰트 설정
FONT_PATH = SC_PATH + "fonts\\NanumGothic.ttf"
FONT_PROP = font_manager.FontProperties(fname=FONT_PATH).get_name()
rc("font", family=FONT_PROP)

# 전체 랭킹 픽률
allrank_pickrate.create_table(DATA_PATH + "allranking_data.csv")    #표



