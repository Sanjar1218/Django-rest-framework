import requests

endpoint = "http://127.0.0.1:8000/home/"

dct = {
    'first':'asdf',
    'dec': 'one',
    'count': 'two',
}

r = requests.post(endpoint, json=dct)
print(r.json())