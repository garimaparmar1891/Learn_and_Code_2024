class TumblerPosts:
    def display_post_images(self, blog_data):
        for idx, post in enumerate(blog_data.posts, start=1):
            print(f"{idx}.")
            if post.photos:
                for photo in post.photos:
                    print(photo.photo_url_1280)
            else:
                print("No photos available for this post.")
