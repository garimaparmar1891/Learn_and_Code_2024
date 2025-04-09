from http import HTTPStatus
from .model import ProductModel
from .productDTO import ProductDTO

class ProductService:
    @staticmethod
    def fetch_products_by_category(category_id):
        products = ProductModel.get_products_by_category(category_id)

        if not products:
            return {"message": "No products found in this category"}, HTTPStatus.OK

        product_list = [
            ProductDTO(
                name=product[0],
                price=product[1],
                quantity_available=product[2]
            ).__dict__ for product in products
        ]

        return product_list, HTTPStatus.OK
