import requests
from config import API_URL

class CartAPIHandler:
    @staticmethod
    def send_get_request(endpoint):
        try:
            return requests.get(f"{API_URL}/{endpoint}").json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return {}

    @staticmethod
    def send_post_request(endpoint, payload):
        try:
            response = requests.post(f"{API_URL}/{endpoint}", json=payload)
            return response.json() if response.status_code == 200 else None
        except requests.exceptions.RequestException:
            print("Error: Unable to connect to the server.")
            return None
