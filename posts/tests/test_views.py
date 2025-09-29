from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from posts.models import Post

# Create your tests here.
class PostCreateViewTest(APITestCase):
    
    def test_create_post_succes(self):
        """
        Should create a post when valid data is sent
        """
        
        url = reverse('post-create')
        
        data = {
            "title": "My last post",
            "content": "This is the content of the post.",
            "category": "C#"
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().title, "My last post")
        
    def test_create_post_invalid_data(self):
        
        
        url = reverse('post-create')
        
        data = {
            "content": "This is the content of the post."
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Post.objects.count(), 0)