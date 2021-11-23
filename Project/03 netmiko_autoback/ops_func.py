import netmiko
import os
import time
import sqlite3 as sql


def get_device_info(db_name, table_name):
    DB = sql.connect(db_name)
    CURSOR = DB.cursor()
    CURSOR.execute(f"select * from {table_name}")
    return CURSOR.fetchall()
    
def create_dict(ori_infos):
    devices = []
    for info in ori_infos:
        device = {}
        device['device_type'] = info[1]
        device['port'] = 22
        device['ip'] = info[2]
        device['username'] = info[3]
        device['password'] = info[4]
        devices.append(device)
    return devices
    
def check_folder(device_path, path):
    if not os.path.isdir(path):
        os.mkdir(path)
    path += device_path + '/'
    if not os.path.isdir(path):
        os.mkdir(path)
        print("{} 目录已建立".format(path))
    return path

def create_filename():
    time_struct = time.localtime()
    str_year = str(time.localtime().tm_year) + "_"
    str_mon = str(time.localtime().tm_mon) + "_"
    str_mday = str(time.localtime().tm_mday) + "_"
    str_hour = str(time.localtime().tm_hour) + "_"
    str_min = str(time.localtime().tm_min) + "_"
    str_sec = str(time.localtime().tm_sec) + ".cfg"
    filename = str_year + str_mon + str_mday + str_hour + str_min + str_sec
    return filename

def save_config(device_type, ip, path, config_data):
    device_path = device_type + '_' + ip
    this_path = check_folder(device_path, path)
    filename = create_filename()
    full_path = this_path + filename
    with open(full_path, 'w') as f:
        f.write(config_data)
        
def backup(config_save_path="config/"):
    ori_infos = get_device_info("NETWORK_OPS", "DB_NETOPS")
    devices = create_dict(ori_infos)
    print("\n\\(˙<>˙)==[配置备份中，活让我干就好，您喝茶]\n")
    for device_info in devices:
        server = netmiko.ConnectHandler(**device_info)
        print("已登入设备：{}".format(device_info["ip"]))
        if device_info['device_type'] == 'cisco_ios':
            config = server.send_command("show running-config")
        elif device_info['device_type'] == 'huawei':
            config = server.send_command("display current-configuration")
        print("已获取配置")
        server.disconnect()
        del server
        save_config(device_info['device_type'], device_info["ip"], config_save_path, config)
        print("已保存配置")
    print("\n\\(˙ω˙)==[备份结束，新备份文件已经就位，请大哥检查]")