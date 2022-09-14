from rest_framework import urlpatterns
from .views import PostList
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

router = DefaultRouter()
router.register('', PostList, basename='post')
# This line tells django urlpatterns is now router.urls
urlpatterns = router.urls
