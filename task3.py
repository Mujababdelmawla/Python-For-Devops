import argparse
from datetime import datetime
import os 
import shutil

def parse_arguments():

    parser = argparse.ArgumentParser(description='A script takes your username and your stats message and log them to a log file')

    parser.add_argument('username', type=str, help='Your username')
    parser.add_argument('status_message', type=str, help='Your status message')
    return parser.parse_args()

def log_message(username, status_message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {username} - {status_message} \n"
    log_file = "./STATUS.LOG"
    with open(log_file, 'a') as file:
        file.write(log_entry)
    print(f"log has been saved to {log_file}")





def analyze_log():
    with open("STATUS.LOG", 'r') as file:
        lines = file.readlines()
        count = len(lines)
        print(f"the total number of entries is : {count}")
        if lines:
            print(f"the last entry is : {lines[-1]}")



def backup_logs():
    log_file = "STATUS.LOG"
    backup_dir = "./BACKUP_FOLDER"
    # create the directory if it doesn't exists
    os.makedirs(backup_dir, exist_ok=True)
    shutil.copy(log_file, backup_dir)
    print(f"the log backedup to {backup_dir}/{log_file}")



def main():
    args = parse_arguments()
    print(f"Hello {args.username}!!!!")
    log_message(args.username, args.status_message)
    analyze_log()
    backup_logs()

if __name__ == "__main__":   
    main()

