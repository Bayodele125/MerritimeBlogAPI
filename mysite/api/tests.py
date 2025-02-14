from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class BlogPostCRUDTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.blogpost_url = reverse("blogpost-view-create")
        self.valid_data = {
            "title": "Test Blog Post",
            "content": "This is a test blog post."
        }
        # Create a blog post
        response = self.client.post(self.blogpost_url, self.valid_data, format="json")
        self.blogpost_id = response.json()["id"]

    def test_retrieve_blogpost(self):
        """Test retrieving a single blog post"""
        response = self.client.get(reverse("update", args=[self.blogpost_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["title"], self.valid_data["title"])

    def test_update_blogpost(self):
        """Test updating a blog post"""
        updated_data = {
            "title": "Updated Title",
            "content": "Updated Content."
        }
        response = self.client.put(reverse("update", args=[self.blogpost_id]), updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["title"], updated_data["title"])

    def test_delete_blogpost(self):
        """Test deleting a blog post"""
        response = self.client.delete(reverse("update", args=[self.blogpost_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(reverse("update", args=[self.blogpost_id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
