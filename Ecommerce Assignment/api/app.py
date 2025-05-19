from flask import Flask
from auth import auth_bp
from categories import categories_bp
from products import products_bp
from cart import cart_bp
from orders import orders_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth_bp)
    app.register_blueprint(categories_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(orders_bp)

    @app.route('/health', methods=['GET'])
    def health_check():
        return {"status": "ok"}, 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=5000, debug=True)
