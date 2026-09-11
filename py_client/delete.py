import requests

product_id = input("Input the product id you want to delete: ")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} is not valid!")

if product_id:
    endpoint = f'http://localhost:8000/products/{product_id}/delete/'
    response = requests.delete(endpoint)
    print(response)

