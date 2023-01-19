import requests
#n = IN[0]
n = 
#s = IN[1]
s = 
#e = IN[2]
e = 
#w = IN[3]
w = 
api_url = "https://data.3dbuildings.com/download.json?token={v6gd3py3wwbdckx4}&w={"+w+"}&s={"+s+"}&e={"+e+"}&n={"+n+"}"
response = requests.get(api_url)
geoJSON = response.json()
status = response.status_code
headers = response.headers["Content-Type"]
OUT = geoJSON, status, headers




Google Maps API

https://maps.googleapis.com/maps/api/staticmap?center=40.714728,-73.998672&zoom=12&size=400x400&maptype=satellite&key=YOUR_API_KEY


3D Buildings Token

Thank you for subscribing to 3dbuildings BUSINESS MAPS.

This is a continuous year-to-year subscription which will automatically renew.
The price will be billed annually as a recurring charge unless you cancel your subscription by emailing us (support@3dbuildings.com) before beginning of your next billing period.

Your API access token is: v6gd3py3wwbdckx4

Documentation about how to use it: https://3dbuildings.com/documentation/
Terms of Service: https://3dbuildings.com/legal/terms/
