import requests

# Making a get request to the API
url = 'https://graph.facebook.com/4/picture?type=large'
r = requests.get(url)

# Saving the image received as binary in jpg format to view it
with open('./UsingWebAPIs/fb_img.jpg', 'wb') as f:
    f.write(r.content)
