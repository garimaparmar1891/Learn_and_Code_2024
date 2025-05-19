class CategoryViewer:
    @staticmethod
    def display(categories):
        print("\nAvailable Categories:")
        for category_id, details in categories.items():
            print(f"{category_id}. {details['name']}")
