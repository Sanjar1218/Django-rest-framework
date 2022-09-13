import requests

endpoint = "http://127.0.0.1:8000/?third=three"

dct = {
    'first':'asdf',
    'first': 'one',
    'second': 'two',
}

r = requests.get(endpoint, params=dct)
print(r.json())