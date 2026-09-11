import requests


endpoint = 'http://localhost:8000/products/'

headers = {
    'Authorization' : 'Blah 5a0fb75b391780d890ed4d3f42714a0ab7875df4' #so we can just do it tru tokens tooo,it's a token of my admin user
}

data = {
    'title' : 'works yeeeeeeeaaaaaaaaaaaaa',
    'price' :900,
}


response = requests.post(endpoint, json=data, headers=headers)

print(response.json())

