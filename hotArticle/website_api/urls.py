# from django.urls import path
# from .views import PostList, PostDetail

# app_name = 'website_api'

# urlpatterns = [
#     path('<str:published>/', PostDetail.as_view(), name='detailcreate'),
#     path('', PostList.as_view(), name='listcreate')
# ]

from .views import PostList
from rest_framework.routers import DefaultRouter

app_name = 'website_api'

router = DefaultRouter()
router.register('', PostList, basename='post')
urlpatterns = router.urls



