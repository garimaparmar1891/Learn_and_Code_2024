import json
from blog_types import BlogData, Post, Photo

class JsonParser:
    def extract_json_from_response(self, response_data):
        if response_data.startswith("var tumblr_api_read ="):
            response_data = response_data.replace("var tumblr_api_read =", "").strip()
            response_data = response_data.rstrip(";")
            return response_data
        else:
            raise ValueError("Unexpected response format from Tumblr API.")

    def convert_json_to_blog_data(self, clean_json):
        data = json.loads(clean_json)
        return BlogData(
            title=data['tumblelog']['title'],
            description=data['tumblelog']['description'],
            name=data['tumblelog']['name'],
            posts_total=data['posts-total'],
            posts=[Post(id=post['id'], photos=[Photo(photo_url_1280=photo['photo-url-1280']) for photo in post.get('photos', [])]) for post in data['posts']]
        )
