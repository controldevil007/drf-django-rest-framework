import requests

endpoint = "https://httpbin.org/"
endpoint = "http://127.0.0.1:8000/"
endpoint = "http://localhost:8000/api/"
get_response = requests.post(endpoint,params={"product_id":123}, json={"title": "Hello world"})
print(get_response.text)
# print(get_response.json())

# HTTP Request -> HTML
# REST API HTTP Request -> JSON

# JavaScriptt Object Notation ~ Python Dict
# print(get_response.status_code)

