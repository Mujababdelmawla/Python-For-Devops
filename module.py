import os 

# get the current working directory 

cwd = os.getcwd()
print(f"the current working directory : {cwd}")

# list files in the current directory 

files = os.listdir()
print(f"files in current directory : {files}")
