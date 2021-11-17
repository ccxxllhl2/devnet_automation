from config import *
from function import *

if __name__ == "__main__":
    # 连接设备获取运维数据
    server = ConnectHandler(**device_info)
    route_data, config_data, interface_data = show_cmd(server, commands)
    # 数据存档生成报告
    dir_path = "report"
    check_dir(dir_path)
    output_route_data(route_data, dir_path)
    output_config_data(config_data, dir_path)
    output_if_data(interface_data, dir_path)
    print("运维结束，报告已生成！")