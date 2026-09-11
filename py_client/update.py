import requests


endpoint = 'http://localhost:8000/products/3/update/'

data = {
    'title' : 'water park',
    'content' : 'in a water park, it was actually just The Water itself originally',
    'price' : 99,
    }

response = requests.put(endpoint, json=data)

print(response)

