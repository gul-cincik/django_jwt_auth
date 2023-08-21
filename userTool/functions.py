import requests

BASE_URL = 'http://127.0.0.1:8000/user/'

def register(username, password):
    url = BASE_URL + 'register/'
    data = {'username': username, 'password': password}
    response = requests.post(url, json=data)
    return response.json()

def login(username, password):
    url = BASE_URL + 'login/'
    data = {'username': username, 'password': password}
    response = requests.post(url, json=data)
    return response.json()

def get_breweries(token, query=None):
    url = BASE_URL + f'breweries/?query={query}' if query else BASE_URL + 'breweries/'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    return response.json()