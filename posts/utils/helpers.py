from posts.models import Post

def get_object(pk):
    """
    Gets a specific post by ID
    """
    
    try:
        # Tries to return the object if it exists
        return Post.objects.get(pk=pk) 
    except Post.DoesNotExist:
        # Returns None if the object does not exist.
        return None  