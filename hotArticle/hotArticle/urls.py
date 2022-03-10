from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(('website.urls', 'website'), namespace='website')),
    path('api/', include(('website_api.urls', 'website_api'), namespace='website_api')),
    path('api-auth/', include(('rest_framework.urls', 'rest_framework'), namespace='rest_framework')),
    path('api/user/', include(('users.urls', 'users'), namespace='users')),
]
