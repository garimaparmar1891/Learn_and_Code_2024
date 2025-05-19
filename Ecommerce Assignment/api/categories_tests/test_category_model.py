import unittest
from http import HTTPStatus
from unittest.mock import patch
from app import create_app

class CategoryRouteTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    @patch("categories.service.CategoryService.get_categories")
    def test_get_categories_success(self, mock_get_categories):
        mock_get_categories.return_value = (
            {"categories": [{"id": 1, "name": "Electronics"}]},
            HTTPStatus.OK
        )

        response = self.app.get("/categories")
        data = response.get_json()

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn("categories", data)
        self.assertEqual(data["categories"][0]["name"], "Electronics")

if __name__ == "__main__":
    unittest.main()
