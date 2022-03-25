from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('', include(('website.urls', 'website'), namespace='website')),
    path('api/', include(('website_api.urls', 'website_api'), namespace='website_api')),
    path('api-auth/', include(('rest_framework.urls', 'rest_framework'), namespace='rest_framework')),
    path('api/user/', include(('users.urls', 'users'), namespace='users')),
    path('schema', get_schema_view(
        title="Website API",
        description="API for Website",
        version="1.0.0"
    ), name='API-schema'),
    path('docs/', include_docs_urls(title='WebsiteAPI'))
]
