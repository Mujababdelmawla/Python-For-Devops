# list of servers 
servers = ["server1","server2","server3","server4"]

# simulated server status using dict

server_status = {
    "server1": "online",
    "server2": "offline",
    "server3": "online",
    "server4": "....."

}

# loop through the servers list 

for server in servers:
    status = server_status.get(server, "unknown") # to get the server status 
    if status == "online":
        print(f"{server} is online .")
    elif status == "offline":
        print(f"{server} is offline .")
    else:
        print(f"{server} status unknown")

