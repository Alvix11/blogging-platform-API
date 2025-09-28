from django.urls import path
from .views import PostListView, PostCreateView, PostGetView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostGetView.as_view(), name='post-get'),
]