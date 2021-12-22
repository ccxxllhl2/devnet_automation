import pandas as pd
from data import create_data
from utils import loop_back_manage
from config import iosXE_netconf_info

file_path = "lo_data.xlsx"

def read_data(path):
    ori_data = pd.read_excel(path)
    data = ori_data.values
    return data
         
def main():
    loop_dev = loop_back_manage(iosXE_netconf_info)
    data = read_data(file_path)
    for line in range(data.shape[0]):
        loop_dev.config_loopback(create_data(*data[line], is_config=True))
        
    loop_dev.get_loopback()

    for line in range(0,5):
        loop_dev.delete_loopback(create_data(data[line][0]))
        
    loop_dev.get_loopback()
    
if __name__ == "__main__":
    main()
