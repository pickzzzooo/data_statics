# 내꺼
import graph_manager


def spec_rank_data_loader(rank, data_list, DATA_PATH):
    # 특정 계급에서의 캐릭터 유저수
    data_dic = {}

    for PATH in data_list:
        index = PATH.replace(DATA_PATH + "char_data\\", "")
        index = index.replace(".csv", "")

        data = graph_manager.pickrate_data_loader(PATH, "계급")
        data_dic[index] = data[rank]
    return data_dic


def create_table(rank, data_list, DATA_PATH, key_arr):
    data_dic = spec_rank_data_loader(rank, data_list, DATA_PATH)
    graph_manager.create_table(data_dic, key_arr)


def create_pie(rank, data_list, DATA_PATH, key_arr):
    data_dic = spec_rank_data_loader(rank, data_list, DATA_PATH)
    graph_manager.create_pie(data_dic, key_arr)

def create_barh(rank, data_list, DATA_PATH, key_arr):
    data_dic = spec_rank_data_loader(rank, data_list, DATA_PATH)
    graph_manager.create_brah(data_dic, key_arr)

def create_wc(rank, data_list, DATA_PATH, key_arr, FONT_PATH):
    data_dic = spec_rank_data_loader(rank, data_list, DATA_PATH)
    graph_manager.create_wc(data_dic, FONT_PATH, key_arr)