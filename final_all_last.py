import requests 
import pandas as pd 
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import shutil
import re 
from datetime import datetime 

# function to scrape website and save data 

def scrape_website():
    url = 'https://bbc.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []
    for article in soup.find_all('a', {'class': 'promo-link'}):
        title = article.get_text()
        link = article.get('href')
        data.append([title, link])

    # save the data to a csv file 
    df = pd.DataFrame(data, columns = ['Title', 'Link'])
    df.to_csv('scraped_data.csv', index = False)

# function to backup logs 

def backup_logs():
    logs_dir = './logs'
    backup_dir = f'path/to/backups/backup {datetime.now().strftime(%Y-%m-%d_%H-%M-%S)}'
    shutil.make_archive(backup_dir, 'zip', logs_dir)


# function to parse logs 

def parse_logs():
    with open('system.log', 'r') as file:
        logs = file.readlines()
        error_logs = [log for log in logs if re.search(r'ERROR', log) ]
        return error_logs


def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'admin@example.com'

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('your_email@example.com', 'your_password')
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

# main Devops pipeline function

def devops_pipeline():
    # step 1: scrape the website
    scrape_website()
    # step 2: backup logs
    backup_logs()   
    # step 3: parse logs for errors
    error_logs = parse_logs()
    # step 4: send email if errors found
    if error_logs:
        send_email('Critical Error Alert', '\n'.join(error_logs))

devops_pipeline()