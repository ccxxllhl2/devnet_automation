"""
CISCO IOS 安全基线检查项目
"""

import re

# 管理用户登录安全检测
def enable_secret_check(config):
    if re.findall(r'enable secret',config):
        return True
    else:
        return False
        
def user_secret_check(config):
    if re.findall(r'username(.|\n)*secret',config):
        return True
    else:
        return False
        
def consle_password_check(config):
    state_1 = re.findall(r'line con 0(.|\n|\r)*password',config)
    state_2 = re.findall(r'line con 0(.|\n)*login authentication',config)
    if (state_1 and state_2) != []:
        return True
    else:
        return False
        
def vty_ssh_check(config):
    if re.findall(r'line vty(.|\n)*transport input ssh',config):
        return True
    else:
        return False
        
def vty_acl_check(config):
    if re.findall(r'line vty 0 4(.|\n)*access-class(.|\n)*line vty 5 15(.|\n)*access-class', config):
        return True
    else:
        return False
        
def vty_login_local_check(config):
    if re.findall(r'line vty(.|\n)*login local', config):
        return True
    else:
        return False
        
def ssh_timeout_check(config):
    if re.findall(r'ip ssh time-out', config):
        return True
    else:
        return False
        
def vty_timeout_check(config):
    if re.findall(r'line vty(.|\n)*exec-timeout', config):
        return True
    else:
        return False
        
def con_timeout_check(config):
    if re.findall(r'line con(.|\n)*exec-timeout', config):
        return True
    else:
        return False
        
def con_timeout_check(config):
    if re.findall(r'line con(.|\n)*exec-timeout', config):
        return True
    else:
        return False
        
def aux_timeout_check(config):
    if re.findall(r'line aux(.|\n)*exec-timeout', config):
        return True
    else:
        return False

# AAA安全检测
def aaa_accounting_check(config):
    if re.findall(r'aaa accounting', config):
        return True
    else:
        return False
        
def aaa_auth_check(config):
    if re.findall(r'aaa new-model', config):
        return True
    else:
        return False
        
def aaa_radius_check(config):
    if re.findall(r'radius-server', config):
        return True
    else:
        return False
        
def aaa_tacacs_check(config):
    if re.findall(r'tacacs-server', config):
        return True
    else:
        return False

# SNMP安全检测
def snmp_enable_check(config):
    if re.findall(r'snmp-server ', config):
        return True
    else:
        return False

def snmp_v3_check(config):
    if re.findall(r'snmp-server host(.|\n)*version 3 auth', config):
        return True
    else:
        return False
        
def snmp_RO_check(config):
    if re.findall(r'RO', config):
        return True
    else:
        return False

# loggin安全检测
def loggin_enable_check(config):
    if re.findall(r'logging (\d)', config):
        return True
    else:
        return False
        
def loggin_source_check(config):
    if re.findall(r'logging source-interface', config):
        return True
    else:
        return False

# 热备安全检测
def vrrp_sec_check(config):
    state_1 = re.findall(r'vrrp',config)
    state_2 = re.findall(r'vrrp(.|\n)*authentication md5',config)
    if (state_1 and state_2) != []:
        return True
    else:
        return False
        
def hsrp_sec_check(config):
    state_1 = re.findall(r'standy',config)
    state_2 = re.findall(r'standby(.|\n)*authentication md5',config)
    if (state_1 and state_2) != []:
        return True
    else:
        return False

# 路由协议安全配置检测
def isis_sec_check(config):
    state_1 = re.findall(r'router isis',config)
    state_2 = re.findall(r'authentication mod md5',config)
    if (state_1 and state_2) != []:
        return True
    else:
        return False
        
def eigrp_sec_check(config):
    state_1 = re.findall(r'router eigrp',config)
    state_2 = re.findall(r'ip authentication mode',config)
    if (state_1 and state_2) != []:
        return True
    else:
        return False
        
def ospf_sec_check(config):
    state_1 = re.findall(r'router ospf',config)
    state_2 = re.findall(r'ip ospf message-digest-key',config)
    if (state_1 and state_2) != []:
        return True
    else:
        return False
        
def rip_sec_check(config):
    state_1 = re.findall(r'router rip',config)
    state_2 = re.findall(r'ip rip authentication mod',config)
    if (state_1 and state_2) != []:
        return True
    else:
        return False
        
def bgp_sec_check(config):
    state_1 = re.findall(r'router bgp',config)
    state_2 = re.findall(r'router bgp(.|\n)*neighbor(.|\n)*password',config)
    if (state_1 and state_2) != []:
        return True
    else:
        return False
        
def bgp_sec_check(config):
    state_1 = re.findall(r'router bgp',config)
    state_2 = re.findall(r'bgp dampenin',config)
    if (state_1 and state_2) != []:
        return True
    else:
        return False
        
def bgp_dampening_check(config):
    if re.findall(r'bgp dampenin',config):
        return True
    else:
        return False
        
def bgp_neighbor_out_filter_check(config):
    if re.findall(r'neighbor(.|\n)*prefix-list(.|\n)*out', config):
        return True
    else:
        return False

# NTP安全检测
def ntp_check(config):
    if re.findall(r'ntp server', config):
        return True
    else:
        return False
        
def ntp_auth_check(config):
    if re.findall(r'ntp authenticate', config):
        return True
    else:
        return False

# TCP保持检测
def tcp_keep_check(config):
    state_1 = re.findall(r'tcp-keepalives-out',config)
    state_2 = re.findall(r'tcp-keepalives-in',config)
    if (state_1 and state_2) != []:
        return True
    else:
        return False

# 不必要协议关闭检测
def cdp_disable_check(config):
    if re.findall(r'no cdp enable', config):
        return True
    else:
        return False
        
def pad_disable_check(config):
    if re.findall(r'no service pad', config):
        return True
    else:
        return False
        
def pad_disable_check(config):
    if re.findall(r'no ip bootp server', config):
        return True
    else:
        return False
        
def source_route_disable_check(config):
    if re.findall(r'no ip source-route', config):
        return True
    else:
        return False
        
def http_disable_check(config):
    if re.findall(r'no ip http server', config):
        return True
    else:
        return False
        
def small_disable_check(config):
    if re.findall(r'no service.*small-servers', config):
        return True
    else:
        return False
        
def finger_disable_check(config):
    if re.findall(r'no ip finger', config):
        return True
    else:
        return False
        
def redirects_disable_check(config):
    if re.findall(r'no ip redirects', config):
        return True
    else:
        return False

# 网络风暴控制检测
def storm_control_check(config):
    if re.findall(r'storm-control broadcast.unicast(.|\n)*multicast', config):
        return True
    else:
        return False