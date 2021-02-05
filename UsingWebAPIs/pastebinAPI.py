import requests
import json

# Making a get request to the API
url = 'https://pastebin.com/api/api_post.php'
parameters = {
    'api_dev_key': 'h3QEccIpCf82JhxQi2X6wcvfkZKs8SEW',
    'api_option': 'paste',
    'api_paste_code': 'Hello World! My name is Ishaan Kamra and I study at Delhi Technological University'
}  # defining the parameters to send in the request
r = requests.post(url, data=parameters)

# Getting the url of the above text pasted in pastebin from the reponse we received from the request
pasted_url = r.content
