import requests
from bs4 import BeautifulSoup

# Making a get request to the URL
url = 'https://www.passiton.com/inspirational-quotes'
r = requests.get(url)

# Getting the html of the page from the reponse we received from the request
html = r.content

# Parsing the data using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Getting the required images and saving them in a separate subfolder
quotes_column = soup.find('div', attrs={'id': 'all_quotes'})
quotes = quotes_column.find_all('img')
for index, quote in enumerate(quotes):
    image_link = quote['src']
    with open(f'./UsingBS4/images/{index+1}.jpg', 'wb') as f:
        f.write(requests.get(image_link).content)
