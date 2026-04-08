class server:
    def __init__(self, name, ip_address):
        self.name = name 
        self.ip_address = ip_address

    def start(self):
        return f"{self.name} with {self.ip_address} is starting ...."

    def stop(self):
        return f"{self.name} with {self.ip_address} is stopping ...."

# creating the object for the server class 

server1 = server("webserver1", "192.168.0.1")

print(server1.name)

print(server1.start())


class DatabaseServer(server):
    def __init__(self, name, ip_address, database_type):
        super().__init__(name, ip_address) # inheriting from server class 
        self.database_type = database_type

    def start(self):
        return f"{self.name} with {self.ip_address} and {self.database_type} database is starting ....."

# create a database object for the databaseserver class

db_server = DatabaseServer("DBserver1","192.168.0.2","MYSQL")

print(db_server.name)
print(db_server.start())


# Inheritance : it is the mechanisem where a new class can take values and methods form an existing class.
