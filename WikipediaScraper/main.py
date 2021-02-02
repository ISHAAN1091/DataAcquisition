from bs4 import BeautifulSoup
import csv
import requests

# Making a get request to the URL
url = 'https://en.wikipedia.org/wiki/Android_version_history'
req = requests.get(url)

# Getting the html of the page from the reponse we received from the request
html = req.content

# Parsing the data using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Getting the required table
table = soup.find_all('table', attrs={'class': 'wikitable'})[0]

# Getting all the
rows = table.find_all('tr')

# Cleaning the collected data
cleanedRows = []
cleanedRow = []
row = rows[0]
rowData = row.find_all('th')
for data in rowData[:-1]:
    temp = data.get_text().replace('\n', '')
    temp = temp.replace('–', '-')
    cleanedRow.append(temp.replace(',', ''))
cleanedRows.append(cleanedRow)
for row in rows[1:]:
    cleanedRow = []
    rowData = row.find_all('td')
    for data in rowData[:-1]:
        temp = data.get_text().replace('\n', '')
        temp = temp.replace('–', '-')
        cleanedRow.append(temp.replace(',', ''))
    cleanedRows.append(cleanedRow)
cleanedRows[2].insert(0, cleanedRows[1][0])

# Storing the cleaned data
with open('./WikipediaScraper/data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in cleanedRows:
        writer.writerow(row)
