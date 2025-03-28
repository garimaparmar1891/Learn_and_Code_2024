from .model import ProductModel

class ProductService:
    @staticmethod
    def fetch_products_by_category(category_id):
        products = ProductModel.get_products_by_category(category_id)

        if not products:
            return {"message": "No products found in this category"}, 200

        return [
            {
                "name": product[0],
                "price": product[1],
                "quantity_available": product[2]
            }
            for product in products
        ], 200
