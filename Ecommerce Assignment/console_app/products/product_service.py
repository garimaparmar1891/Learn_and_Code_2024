import requests
from config import API_URL

class ProductService:
    @staticmethod
    def fetch_products(category_id):
        try:
            response = requests.get(f"{API_URL}/products/{category_id}")
            return response.json() if response.status_code == 200 else []
        except requests.exceptions.RequestException:
            print("\nError: Unable to fetch products. Please try again later.")
            return []
