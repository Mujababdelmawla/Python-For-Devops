from bs4 import BeautifulSoup
import requests

# send a GET request to fetch page content 
url = 'https://bbc.com'
response = requests.get(url)
# parse the HTML content using BeauitfulSoup 
soup = BeautifulSoup(response.text, 'html.parser')
# extract all the links from the page 
for link in soup.find_all('a'):
    print(link.get('href'))