#from os import name
#from rest_framework import urlpatterns
from .views import PostDetail, PostList, PostListDetailFilter
#from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = 'blog_api'

#router = DefaultRouter()
#router.register('', PostList, basename='post')
# This line tells django urlpatterns is now router.urls
#urlpatterns = router.urls

urlpatterns = [
    path('posts/', PostDetail.as_view(), name='detailcreate'),
    path('search/', PostListDetailFilter.as_view(), name='postsearch'),
    path('', PostList.as_view(), name='listcreate'),
]
