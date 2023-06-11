import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud




def pickrate_data_loader(PATH, column):
    # 데이터 딕셔너리
    data_dic = pd.read_csv(PATH)
    allrank_pick_dic = {}

    for char in data_dic[column]:
        if not pd.notna(char): continue
        if not char in allrank_pick_dic:
            allrank_pick_dic[char] = 1
        else:
            allrank_pick_dic[char] += 1

    # 내림차순 정렬
    allrank_pick_dic = dict(sorted(allrank_pick_dic.items(), key=lambda x: x[1], reverse=True))
    return allrank_pick_dic


def convert_percent(data_dic):
    data_dic = dict(sorted(data_dic.items(), key=lambda x: x[1], reverse=True))
    data_list = data_dic.values()

    # 백분율 변환
    all_pick_val = 0

    data_per_dic = {}
    for data in data_list:
        all_pick_val += data
    for char in data_dic:
        data_per_dic[char] = str(
            round(float(data_dic[char]) / float(all_pick_val) * 100, 2))
    return data_per_dic

def create_table(dic, key_arr):
    per_dic = convert_percent(dic)

    per_dic2 = {}
    # 인덱스 값 조정
    rank_cnt = 0
    for char in per_dic:
        rank_cnt += 1
        per_dic2[str(rank_cnt) + ". " + char] = per_dic[char] + "%"

    data_df = pd.DataFrame.from_dict(per_dic2, orient="index", columns=[key_arr[1]])

    # Determine the number of sub-tables based on the desired table width
    table_width = 5  # Number of columns in each sub-table
    num_sub_tables = len(data_df.columns) // table_width + 1

    fig, ax = plt.subplots(1, 1)

    # Create sub-tables and arrange them horizontally
    for i in range(num_sub_tables):
        sub_table = data_df.iloc[:, i * table_width: (i + 1) * table_width]

        table = ax.table(
            cellText=sub_table.values,
            cellLoc='right',
            colLabels=sub_table.columns,
            rowLabels=sub_table.index,
            loc='center'
        )
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        table.scale(1.2, 1.2)
        table.auto_set_column_width([0, 1])
        ax.axis('off')

    plt.suptitle(key_arr[2])  # Add a common title for the entire table
    plt.show()

"""
def create_table(dic, key_arr):
    per_dic = convert_percent(dic)

    per_dic2 = {}
    # 인덱스 값 조정
    rank_cnt = 0
    for char in per_dic:
        rank_cnt += 1
        per_dic2[str(rank_cnt) + ". " + char] = per_dic[char] + "%"

    data_df = pd.DataFrame.from_dict(per_dic2, orient="index", columns=[key_arr[1]])
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
"""

def create_pie(dic, key_arr):
    data_df = pd.DataFrame.from_dict(dic, orient="index", columns=[key_arr[1]])

    plt.pie(data_df[key_arr[1]], labels=data_df.index, autopct="%1.1f%%")
    plt.title(key_arr[2])
    plt.show()


def create_brah(dic, key_arr):
    data_df = pd.DataFrame.from_dict(dic, orient="index", columns=[key_arr[1]])

    color = ['red', 'blue', 'green', 'gray', 'orange', 'purple', 'yellow', 'pink', 'brown', 'black']
    plt.barh(data_df.index, data_df[key_arr[1]], align='center', edgecolor='black', color=color, alpha=0.5)
    plt.xlabel(key_arr[1])
    plt.title(key_arr[2])
    plt.show()


def create_wc(dic, FONT_PATH, key_arr):
    data_df = pd.DataFrame.from_dict(dic, orient="index", columns=[key_arr[1]])

    wc = WordCloud(background_color='black', font_path=FONT_PATH).generate_from_frequencies(
        dict(zip(data_df.index, data_df[key_arr[1]])))

    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title(key_arr[2])
    plt.show()