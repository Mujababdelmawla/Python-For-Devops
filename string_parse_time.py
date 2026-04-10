# strptime : is used to convert a datetime string format into a datetime object

import datetime

user_input_date = "01/03/2026 14:30"

date_object = datetime.datetime.strptime(user_input_date , "%d/%m/%Y %H:%M")
print(date_object)