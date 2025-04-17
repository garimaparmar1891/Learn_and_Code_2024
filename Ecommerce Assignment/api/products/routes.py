from . import products_bp 
from .controller import ProductController

@products_bp.route("/products/<int:category_id>", methods=["GET"])
def get_products_by_category(category_id):
    return ProductController.get_products_by_category(category_id)
