import unittest
from http import HTTPStatus
from unittest.mock import patch
from app import create_app

class CategoryRouteTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    @patch("categories.controller.CategoryController.get_categories", return_value=({"categories": ["Electronics"]}, HTTPStatus.OK))
    def test_get_categories(self, mock_get_categories):
        response = self.app.get("/categories")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn("categories", response.get_json())

if __name__ == "__main__":
    unittest.main()
