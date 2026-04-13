import requests
url = 'https://bbc.com'
response = requests.get(url)

if response.status_code == 200:
    print("webpage fetched successfully.")

else:
    print("failed to fetch the webpage")

print(response.text)
