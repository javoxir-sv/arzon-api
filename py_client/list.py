import requests
from getpass import getpass

auth_endpoint = 'http://localhost:8000/api/auth/'
username = str(input("Username: "))
password = getpass()

auth_response = requests.post(auth_endpoint, json={'username':username, 'password':password})

print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization' : f"Blah {token}"
    }
    print(token)

    endpoint = 'http://localhost:8000/products/'
    get_response = requests.get(endpoint, headers=headers)
    data = get_response.json()
    print(data)

    next_url = data['next']
    results = data['results']
    print("OIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\n", results)


#    if next_url is not None:
#        get_response = requests.get(next_url, headers=headers)