from rest_framework import generics, permissions
from .models import Posts
from .serializers import PostsSerializer

class AllPostsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
