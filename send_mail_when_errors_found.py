import smtplib
from email.mime.text import MIMEText
import re

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'admin@example.com'

    with smtplib.SMTP('smtp.example.com') as server:
    server.login('your_email@example.com', 'your_password')
    server.sendmail(msg['From'], [msg['To']], msg.as_string())
    
# Read logs and parse for errors
with open('system.log', 'r') as file:
    logs = file.readlines()

# find critical errors

critical_errors = [log for log in logs if re.serach(r'ERROR', log)]

if critical_errors:
    send_email('critical error alert', '\n'.join(critical_errors))
    print("Email sent for critical errors.")