import requests
from config import API_KEY, BASE_URL
from exceptions.api_exceptions import APIError

class GeocodingService:
    def get_coordinates(self, place):
        response = self._make_api_request(place)
        data = self._parse_response(response)
        return self._extract_coordinates(data)

    def _make_api_request(self, place):
        params = {
            "q": place,
            "limit": 1,
            "appid": API_KEY
        }
        response = requests.get(BASE_URL, params=params)
        if response.status_code != 200:
            raise APIError(f"API call failed with status code {response.status_code}")
        return response

    def _parse_response(self, response):
        data = response.json()
        if not data:
            raise APIError("No results found for the specified location.")
        return data

    def _extract_coordinates(self, data):
        return {
            "latitude": data[0].get("lat"),
            "longitude": data[0].get("lon")
        }
