from django.urls import path
from .views import AllPostsView, PostDetailView


urlpatterns = [
    path('posts/', AllPostsView.as_view(), name="posts-all"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="post-detail")
]