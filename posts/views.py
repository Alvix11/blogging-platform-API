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
        
        # Obtain data from the database
        posts = Post.objects.all()
        
        # Serialize data (convert to JSON)
        serializer = PostSerializer(posts, many=True)
        
        return Response(serializer.data, status=200)

class PostCreateView(APIView):
    """
    View to create post using APIView
    """
    
    def post(self, request):
        """Handles POST requests (create a post)"""
        
        serializer = PostSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)