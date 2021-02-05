import requests
import json

# Making a get request to the API
url = 'https://maps.googleapis.com/maps/api/geocode/json?'
parameters = {
    'address': 'coding blocks pitampura',
    'key': 'AIzaSyDxpzAOiOie2lqiUfMhWegOvmbKH25TNlE'
}  # defining the parameters to send in the request
r = requests.get(url, params=parameters)

# Getting the JSON data from the reponse we received from the request
json_data = r.content

# Parsing the received JSON data
data = json.loads(json_data)

# Accessing the parsed data
print(data)
