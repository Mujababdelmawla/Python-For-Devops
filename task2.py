class Server:
    def __init__(self, name, ip_address, status): # the constructor methoed and invoke when o object created
        self.name = name 
        self.ip_address = ip_address
        self.status = status 


     # defining the class methods :
    def start(self):
        self.status = "ONLINE"
        return f"the {self.name} server having the {self.ip_address} ip address is {self.status}."
    
    def stop(self):
        self.status = "OFFLINE"
        return f"the {self.name} server having the {self.ip_address} ip address is {self.status}."
    
    def get_status(self):
        
        return f"the {self.name} server having the {self.ip_address} ip address current status is {self.status}"
   

# creating the object for this class 
server1 = Server("FrontEnd", "192.168.0.1", "Online")

# print the methods 

print(server1.name)
print(server1.ip_address)
print(server1.status)
print(server1.start())
print(server1.stop())
print(server1.get_status())


# inheritance from the parent class (Server)

class WebServer(Server):
    def __init__(self, name, ip_address, status, port):
        super().__init__(name, ip_address, status)
        self.port = port 
    def start(self):
        self.status = "ONLINE"
        return f"the {self.name} server having the {self.ip_address} ip address in  {self.status} status is on the port {self.port}"



# create the object for this child class:
server2 = WebServer("BackEnd", "192.168.0.2", "online", "1000")

print(server2.name)
print(server2.ip_address)
print(server2.status)
print(server2.port)
print(server2.start())


class DatabaseServer(Server):
    def __init__(self, name, ip_address, status, db_type):
        super().__init__(name, ip_address, status)
        self.db_type = db_type

    def start(self):
        self.status = "ONLINE"
        return f"the {self.name} server having {self.ip_address} ip address with {self.db_type} database type is {self.status}"


# creating the object for this class 

server3 = DatabaseServer("database", "192.168.0.3", "online", "MYSQL")

print(server3.name)
print(server3.ip_address)
print(server3.status)
print(server3.db_type)
print(server3.start())


# a fuction that log the servers status in server_log.txt file 
def log_status(Server):
    with open('server_log.txt', 'a') as file:
        file.write(f"server:{Server.name} | ip_address:{Server.ip_address} | status:{Server.status}\n")

    print(f"logged {Server.name} successfully" )


log_status(server1)
log_status(server2)
log_status(server3)


# for loop to call each server start and log_status
servers = [server1, server2, server3]
for server in servers:
    print(server.start())
    log_status(server)

