from collections import defaultdict

class OrderViewer:
    @staticmethod
    def display(orders):
        if not orders:
            OrderViewer._print_no_orders()
            return

        grouped_orders = OrderViewer._group_orders_by_id(orders)
        OrderViewer._print_order_summary(grouped_orders)

    @staticmethod
    def _print_no_orders():
        print("\nNo Past Orders !!")

    @staticmethod
    def _group_orders_by_id(orders):
        grouped = defaultdict(list)
        for order in orders:
            grouped[order.get("order_id")].append(order)
        return grouped

    @staticmethod
    def _print_order_summary(grouped_orders):
        print("\nYour Order History:")
        for order_id, items in grouped_orders.items():
            total_amount = OrderViewer._calculate_order_total(items)
            order_date = items[0].get("order_date", "Unknown Date")
            print(f"\nDate: {order_date} - Total: ${total_amount:.2f}")

            for item in items:
                name = item.get('product_name', 'Unknown Product')
                qty = int(item.get('quantity', 1))
                price = float(item.get('price', 0)) * qty
                print(f"  - {name} (Qty: {qty}, Price: ${price:.2f})")

    @staticmethod
    def _calculate_order_total(items):
        return sum(float(item.get("price", 0)) * int(item.get("quantity", 1)) for item in items)
