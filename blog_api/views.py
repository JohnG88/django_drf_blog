from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
# Create your views here.

class PostList(generics.ListCreateAPIView):
    # post_objects is from Model Manager of Post model
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer
    pass

class PostDetail(generics.RetrieveDestroyAPIView):
    pass
