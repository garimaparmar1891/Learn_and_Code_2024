from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Photo:
    photo_url_1280: str # Stores the URL of the photo in 1280px resolution

@dataclass
class Post:
    id: str
    photos: Optional[List[Photo]] = None

@dataclass
class BlogData:
    title: str
    description: str
    name: str
    posts_total: int
    posts: List[Post]
