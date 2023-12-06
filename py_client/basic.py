import requests

endpoint = "https://httpbin.org/"
endpoint = "http://127.0.0.1:8000/"
get_response = requests.get(endpoint,json={"query": "Hello world"})
print(get_response.text)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON

# JavaScriptt Object Notation ~ Python Dict
print(get_response.json())
print(get_response.status_code)

# {'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.31.0', 'X-Amzn-Trace-Id': 'Root=1-657061cc-4a9f25ba217b04981dde24d6'}, 'json': None, 'method': 'GET', 'origin': '49.36.179.61', 'url': 'https://httpbin.org/anything'}