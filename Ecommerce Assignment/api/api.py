from flask import Flask
from api_auth import auth_bp
from api_categories import categories_bp
from api_products import products_bp
from api_cart import cart_bp
from api_orders import orders_bp

api = Flask(__name__)

api.register_blueprint(auth_bp)
api.register_blueprint(categories_bp)
api.register_blueprint(products_bp)
api.register_blueprint(cart_bp)
api.register_blueprint(orders_bp)

@api.route('/health', methods=['GET'])
def health_check():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    api.run(port=5000, debug=True)
