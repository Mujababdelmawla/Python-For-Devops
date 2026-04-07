import os # importing the os module to interact with the operating system 

def check_disk_space(path): # the function that checks the disk space 
     statvfs = os.statvfs(path) # os.statvfs returns information about the file system for the given path
     free_space = statvfs.f_frsize * statvfs.f_bavail # calculate the free sapce by multiplying block size by available blocks
    
     return free_space 

# check the disk space for the root directory 
path = "/"
free_space = check_disk_space(path)
# print the available space in MB
print(f"free space in {path} : {free_space/(1024 * 1024)} MB") # 1KB = 1024 bytes , 1MB = 1024 KB , 1GB = 1024 MB