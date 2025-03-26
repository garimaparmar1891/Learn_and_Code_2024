import requests
from config import API_URL
from utils.check_server import print_server_error

class CategoryAPIHandler:
    @staticmethod
    def get_request(endpoint):
        try:
            response = requests.get(f"{API_URL}/{endpoint}")
            if response.status_code == 200:
                return response.json()
            print(f"Error: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException:
            print_server_error()
        return {}
