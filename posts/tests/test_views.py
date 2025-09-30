from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from posts.models import Post

# Create your tests here.
class PostCreateViewTest(APITestCase):
    
    def test_create_post_success(self):
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
        
        #Verify that it was created in the database and that the title matches
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().title, "My last post")
        
    def test_create_post_invalid_data(self):
        """
        Should fail when sending invalid data (e.g. missing title)
        """
        
        url = reverse('post-create')
        
        data = {
            "content": "This is the content of the post."
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # It should not create anything
        self.assertEqual(Post.objects.count(), 0)

class PostUpdateViewTest(APITestCase):
    
    def setUp(self):
        
        # Create an initial post 
        self.post = Post.objects.create(
            title = "Original title",
            content = "Original content",
            category = "Original category"
        )
        
        self.url = reverse('post-update', kwargs={'pk': self.post.pk})

    def test_update_post_put_success(self):
        """
        Should update a post when valid data is sent
        """
        
        data = {
            "title": "Update title",
            "content": "Update content",
            "category": "C++"
        }

        response = self.client.put(self.url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.post.refresh_from_db()
        
        # Verify changes
        self.assertEqual(self.post.title, "Update title")
        self.assertEqual(self.post.content, "Update content")
        self.assertEqual(self.post.category, "C++")
        
    def test_update_post_put_invalid_data(self):
        """
        Should fail when invalid data is sent
        """
        
        data = {
            "title": "", # title empty
            "content": "Still some content",
            "category": "Go"
        }
        
        response = self.client.put(self.url, data, format="json")
        
        # Should fail with status code 400
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_update_post_patch_success(self):
        """
        Should update a post partially when valid data is sent
        """
        
        data = {
            "content": "Update content"
        }
        
        response = self.client.patch(self.url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.post.refresh_from_db()
        
        # Verify that they are the same and have not been updated
        self.assertEqual(self.post.title, "Original title")
        self.assertEqual(self.post.category, "Original category")
        
        # Verify changes
        self.assertEqual(self.post.content, "Update content")
    
    def test_update_post_patch_invalid_data(self):
        
        data = {
            "content": "", # content empty
        }
        
        response = self.client.patch(self.url, data, format="json")
        
        # Should fail with status code 400
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class PostDeleteViewTest(APITestCase):
    
    def setUp(self):
        
        self.post = Post.objects.create(
            title = "Delete title",
            content = "Delete content",
            category = "Delete category"
        )
        
        self.url = reverse('post-delete', kwargs={'pk': self.post.pk})
    
    def test_delete_post_delete_success(self):
        """
        Should delete a post using as reference your pk
        """
        
        self.assertEqual(Post.objects.count(), 1)
        
        response = self.client.delete(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify that it has been deleted
        self.assertEqual(Post.objects.count(), 0)
    
    def test_delete_post_delete_not_found(self):
        """
        Should return 404 when trying to delete a post that does not exist
        """
        non_existing_url = reverse('post-delete', kwargs={'pk': 9999})
        
        self.assertEqual(Post.objects.count(), 1) # DB unchanged
        
        response = self.client.delete(non_existing_url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Database should remain unchanged when trying to delete a non-existing post
        self.assertEqual(Post.objects.count(), 1)

class PostListViewTest(APITestCase):
    
    def setUp(self):
        
        self.post = Post.objects.create(
            title = "Some title",
            content = "Some content",
            category = "Some category"
        )
        
        self.post1 = Post.objects.create(
            title = "Other title",
            content = "Other content",
            category = "Python"
        )
        
        self.post2 = Post.objects.create(
            title = "Example title",
            content = "Python content",
            category = "Example category"
        )

        self.url = reverse('post-list')
    
    def test_list_posts_get_success(self):
        """
        Should return the posts
        """
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify that it returns 2 results
        self.assertEqual(len(response.data), 3)
        
        # Verify that the titles are in the answer
        titles = [post['title'] for post in response.data]
        self.assertIn("Some title", titles)
        self.assertIn("Other title", titles)
        self.assertIn("Example title", titles)
        
    def test_list_filter_post_get_success(self):
        """
        Should return only posts matching the search term
        """
        
        response = self.client.get(self.url, {"search": "Python"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(len(response.data), 2)