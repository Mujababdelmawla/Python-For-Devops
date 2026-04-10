# strftime is used to convert the datetime object into aa formatted string 

import datetime 

current_time = datetime.datetime.now()
formatted_time = current_time.strftime ("%Y-%m-%d %H:%M:%S")
print(formatted_time)