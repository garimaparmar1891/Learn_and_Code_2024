import requests

class TumblerApi:
    def fetch_api_response(self, api_url):
        response = requests.get(api_url)
        if response.status_code != 200:
            raise Exception(f"HTTP error! Status: {response.status_code}")
        return response.text
