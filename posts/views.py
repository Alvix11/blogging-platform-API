from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostListView(APIView):
    """
    View to list posts using APIView
    """
    
    def get(self, request):
        """Handles GET requests (list all posts)"""
        
        posts = Post.objects.all() # Obtain data from the database
        serializer = PostSerializer(posts, many=True) # Serialize data (convert Django object to JSON)
        return Response(serializer.data, status=200) # Success: returns the list of the posts

class PostCreateView(APIView):
    """
    View to create post using APIView
    """
    
    def post(self, request):
        """Handles POST requests (create a post)"""
        
        serializer = PostSerializer(data=request.data) # Deserialize data (convert JSON to Django object)
        
        if serializer.is_valid(): # Verify if the data is valid
            serializer.save() # Saves in the database
            return Response(serializer.data, status=201) # Success: returns the created post
        
        return Response(serializer.errors, status=400) # Error: returns what failed