from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from .utils.helpers import get_object
from django.db.models import Q

# Create your views here.
class PostListView(APIView):
    """
    View to list posts using APIView.
    """
    
    def get(self, request):
        """
        Handles GET requests (list all posts).
        """
        
        # Access the query param 
        search = request.query_params.get('search')
        
        if search:
            
            # Try to retrieve posts using a word as filter
            posts = Post.objects.filter(
                Q(title__icontains=search) | 
                Q(content__icontains=search) | 
                Q(category__icontains=search)
                )
            
            # Serialize data (convert Django object to JSON) and return the post
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # Obtain data from the database
        posts = Post.objects.all()
        
        # Serialize data (convert Django object to JSON) and return the post
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostCreateView(APIView):
    """
    View to create post using APIView.
    """
    
    def post(self, request):
        """
        Handles POST requests (create a post).
        """
        
        # Deserialize data (convert JSON to Django object)
        serializer = PostSerializer(data=request.data) 
        
        # Verify that it is valid, save in the database and return the post 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Returns what failed
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostGetView(APIView):
    """
    View to retrieve a specific post by primary key (pk).
    """

    def get(self, request, pk):
        """
        Handles GET request to return a single post.
        """
        
        # Try to retrieve the post by ID
        post = get_object(pk)
        
        if post is None:
            # Return 404 if not found
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # Serialize data (convert Django object to JSON) and return the post
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PostUpdateView(APIView):
    """
    View to update a post by primary key (pk).
    """
    
    def put(self, request, pk):
        """
        Handles PUT request to update a post.
        """
        
        # Try to retrieve the post by ID
        post = get_object(pk)
        
        if post is None:
            # Returns 404 if not found
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # Deserialize data (convert JSON to Django object)
        serializer = PostSerializer(post, data=request.data)
        
        # Verify that it is valid, updates the object in the database, and return the post. 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # Returns what failed
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        """
        Handles PATCH request to partially update a post.
        """
        
        # Try to retrieve the post by ID
        post = get_object(pk)
        
        if post is None:
            # Returns 404 if not found
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # Deserialize data (convert JSON to Django object)
        serializer = PostSerializer(post, data=request.data, partial=True)
        
        # Verify that it is valid, updates the object in the database, and return the post. 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # Returns what failed
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDeleteView(APIView):
    """
    View to delete a post by primary key (pk)
    """
    
    def delete(self, request, pk):
        """
        Handles DELETE request to delete a post.
        """
        
        # Try to retrieve the post by ID
        post = get_object(pk)
        
        if post is None:
            # Returns 404 if not found
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # Delete post and return to status 201
        post.delete()
        return Response(status=status.HTTP_202_ACCEPTED)