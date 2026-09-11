import requests


endpoint = 'http://localhost:8000/products/23423524525'


response = requests.get(endpoint)

print(response)
print(response.json())
