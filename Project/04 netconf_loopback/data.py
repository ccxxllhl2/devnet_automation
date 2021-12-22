def create_data(name, des=None, ip=None, mask=None, is_config=False):
    if is_config:
        config_data = """
        <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
         <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
          <interface>
           <Loopback>
            <name>{}</name>
            <description>{}</description>
            <ip>
             <address>
              <primary>
               <address>{}</address>
               <mask>{}</mask>
              </primary>
             </address>
            </ip>
           </Loopback>
          </interface>
         </native>
        </config>
        """.format(name, des, ip, mask)
        print("\n已配置{}环回接口".format(name))
        return config_data

    else:
        delete_data = """
        <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
         <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
          <interface>
           <Loopback operation="delete">
            <name>{}</name>
           </Loopback>
          </interface>
         </native>
        </config>
        """.format(name)
        print("\n已删除{}环回接口".format(name))
        return delete_data
    
    