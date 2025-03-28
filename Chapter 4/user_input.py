class UserInput:
    def get_blog_name(self):
        return input("Enter the Tumblr Blog Name: ").strip()

    def get_blog_range(self):
        range_input = input("Enter the Range (start-end): ")
        try:
            start, end = map(int, range_input.split('-'))
            return start, end
        except ValueError:
            raise ValueError("Invalid format. Please enter the range in 'start-end' format.")
