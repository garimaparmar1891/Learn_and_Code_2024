import requests
from enum import Enum

class HTTPStatus(Enum):
    SUCCESS = 200

class TumblrApi:
    def fetch_api_response(self, api_url):
        response = requests.get(api_url)
        if response.status_code != HTTPStatus.SUCCESS.value:
            raise Exception(f"HTTP error! Status: {response.status_code}")
        return response.text
