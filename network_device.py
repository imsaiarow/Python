
class device:

    def __init__(self,name,type,ip,subnet_mask,gateway,protocol):
        self.name = name
        self.type = type
        self.ip = ip
        self.subnet_mask = subnet_mask
        self.gateway = gateway
        self.protocol = protocol

    def convert_into_dictionairy(self):
        devices = []
        device_dict = {
            self.name : {
                "device_type" : self.type,
                "device_ip" : self.ip,
                "device_subnet_mask" : self.subnet_mask,
                "device_gateway" : self.gateway,
                "device_protocol" : self.protocol
                }
                }
        devices.append(device_dict)

        print(devices)

router = device("cisco9380","router","192.168.0.23","255.255.255.0","192.168.0.1","ssh")
switch = device("nxos8001","switch","192.168.0.24","255.255.255.0","192.168.0.1","telnet")

router.convert_into_dictionairy()
switch.convert_into_dictionairy()
    