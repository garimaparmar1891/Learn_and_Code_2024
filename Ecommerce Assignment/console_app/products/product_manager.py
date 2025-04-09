from products.product_service import ProductService
from cart.cart_modifier import CartModifier

class ProductManager:
    def __init__(self):
        self.cart_modifier = CartModifier()

    def browse_products(self, user_id, category_id):
        products = self._get_products(category_id)
        if not products:
            self._print_no_products_message()
            return

        product_map = self._create_product_map(products)
        self._display_products(products)
        self._handle_user_choice(user_id, product_map)

    def _get_products(self, category_id):
        return ProductService.fetch_products(category_id)

    def _print_no_products_message(self):
        print("\nNo products available in this category.")

    def _create_product_map(self, products):
        return {product['name'].lower(): product for product in products}

    def _display_products(self, products):
        print("\nAvailable Products:")
        for product in products:
            print(f"- {product['name']} -> Price: {product['price']}")

    def _handle_user_choice(self, user_id, product_map):
        while True:
            product_choice = input("\nEnter product name to add to cart (or 'B' to go back): ").strip().lower()
            if product_choice == "b":
                return
            if product_choice in product_map:
                product_name = product_map[product_choice]['name']
                self.cart_modifier.add_to_cart(user_id, product_name)
                return
            print("Invalid product name. Please enter a valid product.")
