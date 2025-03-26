import requests
from config import API_URL
from utils.check_server import is_server_available, print_server_error

class ServerRequestHandler:
    @staticmethod
    def check_server():
        if not is_server_available():
            print_server_error()
            return False
        return True

    @staticmethod
    def send_request(endpoint, data=None):
        try:
            url = f"{API_URL}/{endpoint}"
            response = requests.post(url, json=data) if data else requests.get(url)
            response_data = response.json()

            if response.status_code in [200, 201]:
                return response_data
            else:
                print(f"Error: {response_data.get('error', 'Invalid request')}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error: Unable to connect to the server. {e}")
            return None
