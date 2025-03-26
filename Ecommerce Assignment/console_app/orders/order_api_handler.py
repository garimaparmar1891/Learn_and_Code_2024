import requests
from config import API_URL
from utils.check_server import print_server_error

class OrderAPIHandler:
    @staticmethod
    def send_get_request(endpoint, params=None):
        try:
            response = requests.get(f"{API_URL}/{endpoint}", params=params)
            return response.json() if response.status_code == 200 else []
        except requests.exceptions.RequestException:
            print_server_error()
            return []

    @staticmethod
    def send_post_request(endpoint, data=None):
        try:
            response = requests.post(f"{API_URL}/{endpoint}", json=data)
            return response.json() if response.status_code in [200, 201] else {"error": "Request failed"}
        except requests.exceptions.RequestException:
            print_server_error()
            return {"error": "Request failed"}
