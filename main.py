import requests, json

url = "API LINK"

response = json.loads(requests.get(url).text)

print(response)
