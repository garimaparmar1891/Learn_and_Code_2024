from user_input import UserInput
from tumblr_api import TumblerApi
from json_parser import JsonParser
from blog_info import BlogInfo
from tumblr_posts import TumblerPosts

class TumblerApplication:
    @staticmethod
    def main():
        user_input_service = UserInput()
        tumblr_api_service = TumblerApi()
        json_parser_service = JsonParser()
        blog_info_service = BlogInfo()
        post_service = TumblerPosts()

        blog_name = user_input_service.get_blog_name()
        start, end = user_input_service.get_blog_range()
        
        api_url = TumblerApplication.generate_api_url(blog_name, start, end)

        try:
            response_data = tumblr_api_service.fetch_api_response(api_url)
            clean_json = json_parser_service.clean_api_response(response_data)
            blog_data = json_parser_service.parse_json(clean_json)

            blog_info_service.display_blog_info(blog_data)
            post_service.display_post_images(blog_data)
        except Exception as e:
            print(f"An error occurred: {e}")


    @staticmethod
    def generate_api_url(blog_name, start, end):
        return f"https://{blog_name}.tumblr.com/api/read/json?type=photo&num={end - start + 1}&start={start - 1}"


if __name__ == "__main__":
    TumblerApplication.main()
