import requests
import json

url = "https://api.openaq.org/v2/cities?limit=100&page=1&offset=0&sort=asc&order_by=city"

headers = {"accept": "application/xml"}

response = requests.get(url, headers=headers)

print(response.text)
#print(data)
#temperature = data['results']['country']
#print(temperature)
#data = json.loads(response.text)
#print(response.text)
