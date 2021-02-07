import requests
import csv
import json

url = 'http://api.icndb.com/jokes/'

testCases = []
with open('./UsingWebAPIs/ID.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == 'ID':
            continue
        testCases.append(row[0])

finalData = {}

i = 0
for testCase in testCases:
    json_data = requests.get(url+f'{testCase}').content
    data = json.loads(json_data)
    finalData[testCase] = data['value']['joke']
    print(i)
    i += 1

with open('./UsingWebAPIs/data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Joke'])
    for item in finalData:
        writer.writerow([item, finalData[item]])
