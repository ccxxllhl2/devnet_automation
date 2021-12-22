import xmltodict
from ncclient import manager

def show_loopback(interface):
        if_name = interface["name"]
        if_des = interface["description"]
        if_ip = interface["ip"]["address"]["primary"]["address"]
        if_mask = interface["ip"]["address"]["primary"]["mask"]
        print("\n---------------------\n")
        print(f"接口名称:{if_name}")
        print(f"接口描述:{if_des}")
        print(f"接口IP:{if_ip}")
        print(f"接口掩码:{if_mask}")

class loop_back_manage():
    def __init__(self, iosXE_netconf_info):
        self.device = manager.connect(**iosXE_netconf_info)
        
    def get_loopback(self, source="running"):
        full_config = self.device.get_config(source=source)
        xml_data = full_config.xml
        if_data = xmltodict.parse(xml_data)["rpc-reply"]["data"]["native"]["interface"]
        if 'Loopback' in if_data.keys():
            if type(if_data["Loopback"]) is list:
                for data in if_data["Loopback"]:
                    show_loopback(data)
            else:
                show_loopback(if_data["Loopback"])
        else:
            return "没有配置环回接口"
                
    def config_loopback(self, config_data):
        _ops_result = self.device.edit_config(target="candidate", config=config_data)
        self.device.commit()
            
    def delete_loopback(self, delete_data):
        _ops_result = self.device.edit_config(target="candidate", config=delete_data)
        self.device.commit()
            
    def restore_candidate(self):
        ops_replay = self.device.discard_changes()