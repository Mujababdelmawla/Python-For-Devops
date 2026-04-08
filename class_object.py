class server:
    def __init__(self, name, ip_address): # __init__ constructor method 
        self.name = name 
        self.ip_address = ip_address

    def start(self): # method 
        return f"{self.name} with {self.ip_address} is starting ...."

    def stop(self): # method 
        return f"{self.name} with {self.ip_address} is stoping"

# Creating an boject for the server class 
server1 = server("webserver1", "192.168.0.1")

# Accessing attributes and methods 
print(server1.name)

print(server1.ip_address)

print(server1.start())

print(server1.stop())



# A class : is just a blue print or a logical plan (design / template) .
# An object is the real time data that help to perform the locial plan of the class .