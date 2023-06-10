import pandas as pd
import matplotlib.pyplot as plt

def pickrate_data_helper(PATH):
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
    allrank_pick_list = allrank_pick_dic.values()

    # 백분율 변환
    all_pick_val = 0

    allrank_pickrate_dic = {}
    for data in allrank_pick_list:
        all_pick_val += data
    for char in allrank_pick_dic:
        allrank_pickrate_dic[char] = str(
            round(float(allrank_pick_dic[char]) / float(all_pick_val) * 100, 2))
    return allrank_pickrate_dic

def create_table(PATH):
    allrank_pickrate_dic = pickrate_data_helper(PATH)
    allrank_pickrate_dic2 = {}

    rank_cnt = 0
    for char in allrank_pickrate_dic:
        rank_cnt += 1
        allrank_pickrate_dic2[str(rank_cnt) + ". " + char] = allrank_pickrate_dic[char] + "%"

    allrank_pickrate_df = pd.DataFrame.from_dict(allrank_pickrate_dic2, orient="index", columns=["픽률"])

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
    plt.show()
