from services.geocoding_service import GeocodingService
from utils.input_handler import get_place_input
from utils.response_parser import display_coordinates
from exceptions.api_exceptions import APIError

def main():
    place = get_place_input()
    service = GeocodingService()

    try:
        coordinates = service.get_coordinates(place)
        display_coordinates(coordinates)
    except APIError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
