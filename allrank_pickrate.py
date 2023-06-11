#내꺼
import graph_manager


# key_arr = [data columns, df columns, plt title"]
def create_table(PATH, key_arr):
    # 데이터 불러오기
    allrank_pick_dic = graph_manager.pickrate_data_loader(PATH, key_arr[0])
    graph_manager.create_table(allrank_pick_dic, key_arr)

def create_pie(PATH, key_arr):
    data = graph_manager.pickrate_data_loader(PATH, key_arr[0])
    graph_manager.create_pie(data, key_arr)

def create_barh(PATH, key_arr):
    data = graph_manager.pickrate_data_loader(PATH, key_arr[0])
    graph_manager.create_brah(data, key_arr)

def create_wc(DATA_PATH, FONT_PATH, key_arr):
    data = graph_manager.pickrate_data_loader(DATA_PATH, key_arr[0])
    graph_manager.create_wc(data, FONT_PATH, key_arr)