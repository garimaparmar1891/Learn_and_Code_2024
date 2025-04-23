from tumblr_api import TumblrApi
from json_parser import JsonParser
from blog_info import BlogInfoDisplay
from tumblr_posts import TumblerPosts

class TumblerApplication:
    @staticmethod
    def main():
        tumblr_api_service = TumblrApi()
        json_parser_service = JsonParser()
        blog_info_service = BlogInfoDisplay()
        post_service = TumblerPosts()

        blog_name = TumblerApplication._get_blog_name()
        start, end = TumblerApplication._get_blog_range()
        
        api_url = TumblerApplication.generate_api_url(blog_name, start, end)

        try:
            response_data = tumblr_api_service.fetch_api_response(api_url)
            clean_json = json_parser_service.extract_json_from_response(response_data)
            blog_data = json_parser_service.convert_json_to_blog_data(clean_json)

            blog_info_service.display_blog_info(blog_data)
            post_service.display_post_images(blog_data)
        except Exception as e:
            print(f"An error occurred: {e}")


    @staticmethod
    def generate_api_url(blog_name, start, end):
        return f"https://{blog_name}.tumblr.com/api/read/json?type=photo&num={end - start + 1}&start={start - 1}"

    @staticmethod
    def _get_blog_name():
        return input("Enter the Tumblr Blog Name: ").strip()

    @staticmethod
    def _get_blog_range():
        range_input = input("Enter the Range (start-end): ")
        try:
            start, end = map(int, range_input.split('-'))
            return start, end
        except ValueError:
            raise ValueError("Invalid format. Please enter the range in 'start-end' format.")

if __name__ == "__main__":
    TumblerApplication.main()
