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
        
        return f"the {self.name}server with {self.ip_address} ip address current status is {self.status}"


# create the object ofr the Server class
server1 = Server("BackEnd", "192.168.3.2", "up")

print(server1.start())
print(server1.stop())



class WebServer(Server):
    def __init__(self, name, ip_address, status, port):
        super().__init__(name, ip_address, status)
        self.port = port 


    def start(self):
        self.status = "online"
        return f"the {self.name} server  with {self.ip_address} ip address is {self.status} in port {self.port}"


# create an boject 
server2 = WebServer("FrontEnd", "192.168.3.4", "up", "8080")
print(server2.start())


class DatabaseServer(Server):
    def __init__(self, name, ip_address, status, db_type):
        super().__init__(name, ip_address, status)
        self.db_type = db_type

    def start(self):
        self.status = "online"
        return f"the {self.name} server with {self.ip_address} ip address with type {self.db_type} is {self.status} "

# create an object 
server3 = DatabaseServer("DBServer", "192.168.4.6", "up", "MYSQL")

print(server3.start())