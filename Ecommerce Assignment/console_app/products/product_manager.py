from products.product_service import ProductService
from cart.cart_modifier import CartModifier

class ProductManager:
    def __init__(self):
        self.cart_modifier = CartModifier()

    def browse_products(self, user_id, category_id):
        products = ProductService.fetch_products(category_id) 
        if not products:
            print("\nNo products available in this category.")
            return

        product_map = {product['name'].lower(): product for product in products}

        for product in products:
            print(f"- {product['name']} -> Price: {product['price']}")

        self.handle_user_choice(user_id, product_map)

    def handle_user_choice(self, user_id, product_map):
        while True:
            product_choice = input("\nEnter product name to add to cart (or 'B' to go back): ").strip().lower()

            if product_choice == "b":
                return

            if product_choice in product_map:
                self.cart_modifier.add_to_cart(user_id, product_map[product_choice]['name'])
                break
            else:
                print("Invalid product name. Please enter a valid product.")
