from collections import defaultdict

class OrderViewer:
    @staticmethod
    def display(orders):
        if not orders:
            print("\nNo Past Orders !!")
            return

        grouped_orders = defaultdict(list)
        for order in orders:
            grouped_orders[order.get("order_id")].append(order)

        print("\nYour Order History:")
        for order_id, items in grouped_orders.items():
            total_amount = sum(float(item.get("price", 0)) * int(item.get("quantity", 1)) for item in items)
            order_date = items[0].get("order_date", "Unknown Date")

            print(f"\nDate: {order_date} - Total: ${total_amount:.2f}")

            for item in items:
                print(f"  - {item.get('product_name', 'Unknown Product')} "
                      f"(Qty: {item.get('quantity', 1)}, Price: ${float(item.get('price', 0)) * int(item.get('quantity', 1)):.2f})")
