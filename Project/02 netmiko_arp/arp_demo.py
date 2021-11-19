from playarp import playARP


connect_info_dict= {
    "device_type": "cisco_ios",
    "host": "192.168.1.50",
    "username": "ciscouser",
    "secret": "cisco123",
    "password": "cisco@123",
}

arp_task = {"1.1.1.1": "aaaa.aaaa.aaaa",
            "2.2.2.2": "bbbb.bbbb.bbbb",
            "3.3.3.3": "cccc.cccc.cccc",
            "192.168.1.100": "0fa2.2bce.0109"}

def main():
    my_arp = playARP(connect_info_dict)

    # 获取添加ARP之前的ARP表
    my_arp.get_arp()

    # 批量添加ARP
    print("\n开始批量添加ARP")
    for ip in arp_task:
        mac = arp_task[ip]
        my_arp.add_arp(ip, mac)
    my_arp.get_arp()

    # 批量删除ARP
    print("\n开始批量删除ARP")
    for ip in arp_task:
        my_arp.del_arp(ip)
    my_arp.get_arp()
    
    my_arp.net.disconnect()
    
if __name__ == "__main__":
    main()