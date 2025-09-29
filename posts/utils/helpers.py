from posts.models import Post

def get_object(pk):
    """Gets a specific post by ID"""
    
    try:
        return Post.objects.get(pk=pk) # Tries to return the object if it exists
    except Post.DoesNotExist:
        return None  # Returns None if the object does not exist.