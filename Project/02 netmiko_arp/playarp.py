#优化内容：
## add_arp做完ARP添加后不再执行get_arp，方便批量添加
## del_arp做完ARP添加后不再执行get_arp，方便批量删除
## get_arp可以由工程师完成

import re
from netmiko import ConnectHandler

class playARP():
    def __init__(self, connect_info_dict):
        self.net = ConnectHandler(**connect_info_dict)
        self.ip_pattern = r"^(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])$"
        self.mac_pattern = r"^([A-F0-9]{4}\.[A-F0-9]{4}\.[A-F0-9]{4}|[a-f0-9]{4}\.[a-f0-9]{4}\.[a-f0-9]{4})$"
        self.type_pattern = r"^(arpa|sap|smds|snap|srp-a|srp-b)$"
        self.add_ip_list = []
        
    def _connect_device(self):
        if not self.net.is_alive():
            self.net = ConnectHandler(**connect_info_dict)
            print(f"连接成功，当前提示符为{self.net.find_prompt()}")
        
    def get_arp(self):
        self._connect_device()
        self.net.enable()
        print(self.net.send_command("show ip arp"))
        
    def add_arp(self, ip, mac, arp_type="arpa"):
        self._connect_device()
        if not re.search(self.ip_pattern, ip):
            print("IP地址格式错误")
        elif not re.search(self.mac_pattern, mac):
            print("MAC地址格式错误")
        elif not re.search(self.type_pattern, arp_type):
            print("ARP类型错误")
        else:
            self.net.send_config_set(f"arp {ip} {mac} {arp_type}")
            self.add_ip_list.append(ip)
            
    def del_arp(self, ip):
        self._connect_device()
        if not re.search(self.ip_pattern, ip):
            print("IP地址格式错误")
        elif ip not in self.add_ip_list:
            print("此IP地址并没有通过<add_arp>添加过")
        else:
            self.net.send_config_set(f"no arp {ip}")
            self.add_ip_list.remove(ip)