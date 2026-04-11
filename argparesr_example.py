import argparse

parser = argparse.ArgumentParser(description='A simple user login script')

# Add the arguments to the parser 

parser.add_argument('username', type=str, help='Your username')
parser.add_argument('password', type=str, help='Your password')

# parse the args

args = parser.parse_args()

# use args 
print(f"Hello , {args.username} ! : Your password is :{args.password}")
