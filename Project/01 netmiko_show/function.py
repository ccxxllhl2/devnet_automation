import os
from netmiko import ConnectHandler


def show_cmd(server, commands):
    results = []   
    for cmd in commands:
        info = server.send_command(cmd)
        results.append(info)
    server.disconnect()
    
    route_data = results[0]
    config_data = results[1]
    interface_data = results[2]
        
    return route_data, config_data, interface_data
    
def check_dir(dir_path):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        
def output_route_data(route_data, dir_path):
    output_data = route_data.split("\n\n")[-1]
    with open(dir_path + "/route.txt", "w") as file:
        file.write(output_data)
        
def output_config_data(config_data, dir_path):
    output_data = config_data
    with open(dir_path + "/config.txt", "w") as file:
        file.write(output_data)
        
def output_if_data(interface_data, dir_path):
    output_data = interface_data
    with open(dir_path + "/if.txt", "w") as file:
        file.write(output_data)