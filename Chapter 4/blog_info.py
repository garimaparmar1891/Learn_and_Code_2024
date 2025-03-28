class BlogInfo:
    def display_blog_info(self, blog_data):
        print(f"\nTitle: {blog_data.title}")
        print(f"Name: {blog_data.name}")
        print(f"Description: {blog_data.description}")
        print(f"Number of Posts: {blog_data.posts_total}\n")
