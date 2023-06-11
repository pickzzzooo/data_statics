import pandas as pd
import matplotlib.pyplot as plt
import PIL, glob, json
from matplotlib import font_manager, rc

# 내꺼
import graph_manager

# 폰트 설정 / json
FONT_PATH = "C:\\Users\\test2\\Downloads\\data_sicence\\fonts\\NanumGothic.ttf"
FONT_PROP = font_manager.FontProperties(fname=FONT_PATH).get_name()
rc("font", family=FONT_PROP)

with open("rank_point.json", "r", encoding="UTF-8") as file:
    rank_point = json.load(file)


def meta_point_cal(CHAR_LIST):
    data_dic = {}
    for PATH in CHAR_LIST:
        index = PATH.replace("C:\\Users\\test2\\Downloads\\data_sicence\\data\\char_data\\", "")
        index = index.replace(".csv", "")
        data = graph_manager.pickrate_data_loader(PATH, "계급")
        data_dic[index] = 0

        for rank in data:
            if not pd.notna(rank): continue

            point = int(rank_point[rank]) * int(data[rank])
            data_dic[index] += point
    return data_dic


def create_table(data, key_arr):
    data_df2 = {}
    # 인덱스 값 조정
    rank_cnt = 0
    for char in data:
        rank_cnt += 1
        data_df2[str(rank_cnt) + ". " + char] = str(data[char]) + "pt"

    data_df = pd.DataFrame.from_dict(data_df2, orient="index", columns=[key_arr[1]])
    # 표 그리기
    fig, ax = plt.subplots(1, 1)
    table = ax.table(
        cellText=data_df.values,
        cellLoc='right',
        colLabels=data_df.columns,
        rowLabels=data_df.index,
        loc='center'
    )
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.2)
    table.auto_set_column_width([0, 1])
    ax.axis('off')
    plt.title(key_arr[2])
    plt.show()