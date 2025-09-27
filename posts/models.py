from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField()
    tags = ArrayField(
        models.CharField(max_length=50),
        blank=True,
        default=list
        )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title