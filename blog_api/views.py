from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissions, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.

# making custom permissions, to only allow logged in users to edit/delete own posts
class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # matching post author with logged in user
        return obj.author == request.user

class PostList(viewsets.ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer
   # queryset = Post.post_objects.all()

    # override get_object, will fire off with name/number in url
    # When add slug to url ex. http://127.0.0.1:8000/api/new1/, item with slug of new1 will be queried
    def get_object(self, queryset=None, **kwargs):
        # pk is in urls already
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)
    
    # define custom queryset
    def get_queryset(self):
        return Post.objects.all()


#class PostList(viewsets.ViewSet):
#    '''This ViewSet needs router to create auto urls'''
#    permission_classes = [IsAuthenticated]
#    queryset = Post.objects.all()

#    def list(self, request):
#       serializer_class = PostSerializer(self.queryset, many=True)
#       return Response(serializer_class.data)
   
#    def retrieve(self, request, pk=None):
#        post = get_object_or_404(self.queryset, pk=pk)
#        serializer_class = PostSerializer(post)
#        return Response(serializer_class.data)

    '''All functions that can be called in ViewSet'''
    # def list(self, request):
    #     pass
    '''For post functionality'''
    # def create(self, request):
    #     pass
    '''For single object'''
    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
 
#class PostList(generics.ListCreateAPIView):
#    permission_classes = [IsAuthenticatedOrReadOnly]
    # post_objects is from Model Manager of Post model
#    queryset = Post.post_objects.all()
#    serializer_class = PostSerializer

#class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#    permission_classes = [PostUserWritePermission]
#    queryset = Post.post_objects.all():
     #serializer_class = PostSerializer   #     pass
