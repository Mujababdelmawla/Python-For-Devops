# command line arguments help us to pass a certain data to our script while execution time 

# sys.srgv : is the list that contains the command line argument passed to the script 

import sys 

# check it correct number of arguments are passed 
if len(sys.argv) != 3:
    print("Usage: python3 cmd_line_arguments.py <username> <password>")
    sys.exit(1)

# Retrieve args

# argv[0] = script name 

username = sys.argv[1]
password = sys.argv[2]

print(f"Hello, {username} : Your Password Is {password}")