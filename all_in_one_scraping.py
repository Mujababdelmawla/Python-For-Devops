import os 
import requests
import csv 
from bs4 import BeautifulSoup

# define the custom directory path 
custom_path = "./articles.csv"

# Ensure the folder exist (if not, create it ..)
os.makedirs(os.path.dirname(custom_path), exist_ok=True)

# send a GET request to the website to get the website data information
url = 'https://bbc.com'
response = requests.get(url)

# parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# open the csv file at the custom path to write the data
with open(custom_path, 'w', newline='') as file:
    writer = csv.writer(file)

    # write the csv header
    writer.writerow(['title', 'link'])

    # find article titles and links
    articles = soup.find_all('a', href=True)

    # loop through each article and extract the title and link 
    for article in articles:
        title = article.get_text(strip=True) # get the text of the title 
        link = article['href'] # get the href attribute(URL)

        # Ensure full url if the link is relative
        if link.startswith('/'):
            link = 'https://bbc.com' + link

        # only save articles that contain a link (optional check to exclude unrelated links)
        if title and link:
            writer.writerow([title, link]) 


# confirm that the file is saved 
print(f"Data saved to : {custom_path} successfully.!!!")