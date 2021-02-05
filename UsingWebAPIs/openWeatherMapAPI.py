import requests
import json

# Making a get request to the API
url = 'https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b0f5d9d2aa80b451465a8bde95d370d2'
r = requests.get(url)

# Getting the JSON data from the reponse we received from the request
json_data = r.content

# Parsing the received JSON data
data = json.loads(json_data)

# Accessing the parsed data
print(data['coord'])
print(data['weather'][0]['main'], " : ", data['weather'][0]['description'])
