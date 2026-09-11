import requests


endpoint = 'http://localhost:8000/api/'

response = requests.post(endpoint, json={"title" : "I don't know really", 'price':134,})
print(response.text)
print(response.status_code)
print(response.json)
