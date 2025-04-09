import requests
from http import HTTPStatus
from config import API_URL

def is_server_available():
    try:
        response = requests.get(f"{API_URL}/health")
        return response.status_code == HTTPStatus.OK
    except requests.exceptions.RequestException:
        return False  

def print_server_error():
    print("Error: Unable to connect to the server. Please try again later.")
