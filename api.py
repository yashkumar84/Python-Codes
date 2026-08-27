import requests

response = requests.get("https://fakestoreapi.com/products")
print(response.status_code)
print(response.json())

product = {'title': 'Yash Product', 'price': 29.99}

response1 = requests.post("https://fakestoreapi.com/products" , json=product)
print(response1.status_code)
print(response1.json())

product = {'title': 'Updated Product', 'price': 39.99}
response = requests.put('https://fakestoreapi.com/products/1', json=product)
print(response.json())

response = requests.delete('https://fakestoreapi.com/products/1')
print(response.json())

