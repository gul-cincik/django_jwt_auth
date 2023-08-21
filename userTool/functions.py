import requests

BASE_URL = 'http://127.0.0.1:8000/user/'

def register(username, password):
    """
    Registers a new user.

    Args:
        username (str): Username of the user.
        password (str): Password of the user.

    Returns:
        dict: username 
    """
    url = BASE_URL + 'register/'
    data = {'username': username, 'password': password}
    response = requests.post(url, json=data)
    return response.json()

def login(username, password):
    """
    Logs in a user and obtains a JWT token.

    Args:
        username (str): Username of the user.
        password (str): Password of the user.

    Returns:
        dict: JSON response containing JWT token.
    """
    url = BASE_URL + 'login/'
    data = {'username': username, 'password': password}
    response = requests.post(url, json=data)
    return response.json()

def get_breweries(token, query=None):
    """
    Fetches brewery data using a JWT token.

    Args:
        token (str): JWT token obtained after login.
        query (str, optional): Query parameter for filtering breweries. Defaults to None.

    Returns:
        dict: JSON response containing brewery data.
    """
    url = BASE_URL + f'breweries/?query={query}' if query else BASE_URL + 'breweries/'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    return response.json()