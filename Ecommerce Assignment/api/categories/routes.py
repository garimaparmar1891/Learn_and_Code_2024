from flask import jsonify
from . import categories_bp
from .controller import CategoryController

@categories_bp.route("/categories", methods=["GET"])
def get_categories():
    return CategoryController.get_categories()
