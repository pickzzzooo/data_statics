import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import PIL

def pickrate_data_loader(PATH):
    # 데이터 딕셔너리
    data_dic = pd.read_csv(PATH)
    allrank_pick_dic = {}

    for char in data_dic["캐릭터"]:
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

def create_table(PATH):
    # 데이터 불러오기
    allrank_pick_dic = pickrate_data_loader(PATH)
    allrank_pickrate_dic = convert_percent(allrank_pick_dic)

    allrank_pickrate_dic2 = {}
    # 인덱스 값 조정
    rank_cnt = 0
    for char in allrank_pickrate_dic:
        rank_cnt += 1
        allrank_pickrate_dic2[str(rank_cnt) + ". " + char] = allrank_pickrate_dic[char] + "%"

    allrank_pickrate_df = pd.DataFrame.from_dict(allrank_pickrate_dic2, orient="index", columns=["유저 수"])
    # 표 그리기
    fig, ax = plt.subplots(1, 1)
    table = ax.table(
        cellText=allrank_pickrate_df.values,
        cellLoc='right',
        colLabels=allrank_pickrate_df.columns,
        rowLabels=allrank_pickrate_df.index,
        loc='center'
    )
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.2)
    table.auto_set_column_width([0, 1])
    ax.axis('off')
    plt.title("상위 1만명 각 캐릭터의 유저 비율")
    plt.show()

def create_pie(PATH):
    data = pickrate_data_loader(PATH)
    data_df = pd.DataFrame.from_dict(data, orient="index", columns=["유저 수"])

    plt.pie(data_df["유저 수"], labels=data_df.index, autopct="%1.1f%%")
    plt.title("상위 1만명 각 캐릭터의 유저 비율")
    plt.show()

def create_barh(PATH):
    data = pickrate_data_loader(PATH)
    data_df = pd.DataFrame.from_dict(data, orient="index", columns=["유저 수"])

    color = ['red', 'blue', 'green', 'gray', 'orange', 'purple', 'yellow', 'pink', 'brown', 'black']
    plt.barh(data_df.index, data_df["유저 수"], align='center', edgecolor='black', color=color, alpha=0.5)
    plt.xlabel("유저 수")
    plt.title("상위 1만명 각 캐릭터의 유저 수")
    plt.show()

def create_wc(DATA_PATH, FONT_PATH):
    data = pickrate_data_loader(DATA_PATH)
    data_df = convert_percent(data)
    data_df = pd.DataFrame.from_dict(data, orient="index", columns=["유저 수"])

    wc = WordCloud(background_color='black', font_path=FONT_PATH).generate_from_frequencies(
        dict(zip(data_df.index, data_df['유저 수'])))

    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()