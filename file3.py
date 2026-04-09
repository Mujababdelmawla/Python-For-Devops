class Server:
    def __init__(self, name, ip_address, status):
        self.name = name 
        self.ip_address = ip_address
        self.status = status 


    def start(self):
        self.status = "online"
        return f"the {self.name}server with {self.ip_address} ip address is {self.status}"

    def stop(self):
        self.status = "offline"
        return f"the {self.name}server with {self.ip_address} ip address is {self.status}"

    def get_status(self):
        self.status = "up"
        
        return f"the {self.name}server with {self.ip_address} ip address current status is {self.status}"


# create the object ofr the Server class
server1 = Server("BackEnd", "192.168.3.2", "up")

print(server1.start())
print(server1.stop())
print(server1.get_status())
