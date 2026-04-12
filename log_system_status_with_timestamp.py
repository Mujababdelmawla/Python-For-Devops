from datetime import datetime 

# get the current date time 
current_time = datetime.now() # datetime.now 
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S") # strftime

# create a system status message
status_message = f"System Checked {formatted_time} , Everything Is Working Smoothly.... " # f string format

# write the status message to a log file 
log_file = "./system_status.log"
with open(log_file, 'a') as file:  # 'a' append the result every time we run the script 
    file.write(status_message + "\n")
print(f"log has been saved in {log_file}")
