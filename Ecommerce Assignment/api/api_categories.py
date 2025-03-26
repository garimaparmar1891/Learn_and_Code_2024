from flask import Blueprint, jsonify
from api_database import get_database_connection

categories_bp = Blueprint('categories', __name__)

class CategoryController:
    @staticmethod
    @categories_bp.route("/categories", methods=["GET"])
    def get_categories():
        response, status = CategoryService.fetch_categories()
        return jsonify(response), status
    
class CategoryService:
    @staticmethod
    def fetch_categories():
        categories = CategoryModel.get_all_categories()

        if not categories:
            return {"message": "No categories found"}, 200

        return {
            str(row[0]): {"name": row[1]} for row in categories
        }, 200
    

class CategoryModel:
    @staticmethod
    def get_all_categories():
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id, name FROM categories")
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()
