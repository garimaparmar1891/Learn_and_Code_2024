from flask import Blueprint, jsonify
from api_database import get_database_connection

products_bp = Blueprint("products", __name__)

class ProductController:
    @staticmethod
    @products_bp.route("/products/<int:category_id>", methods=["GET"])
    def get_products_by_category(category_id):
        response, status = ProductService.fetch_products_by_category(category_id)
        return jsonify(response), status
    

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
    

class ProductModel:
    @staticmethod
    def get_products_by_category(category_id):
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT name, price, quantity_available FROM Products WHERE category_id = ?",
                (category_id,),
            )
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()
