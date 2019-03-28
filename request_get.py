import requests

def get_url_json(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

def get_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response
    except requests.ConnectionError:
        return None