import requests

headers = {"Authorization": "Bearer fd106f9fa2248f38157d7c5fd8da21f57383d0c8"}
endpoint = "http://localhost:8000/api/products/"

data = {"title": "This field is done"}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
