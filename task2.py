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



# log file to save instead of printing it to the terminal 

def log_status(Server):
    with open ('server_log.txt', 'a') as file:
        file.write(f"server :{Server.name}\n ip address :{Server.ip_address}\n status :{Server.status}\n")
          
    print(f"logged {Server.name} status successfully")



log_status(server1)

log_status(server2)

log_status(server3)



servers = [ server1, server2, server3]
for server in servers:
    print(server.start())
    log_status(server)