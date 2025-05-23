"""
URL configuration for connectly_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.conf import settings
from django.conf.urls.static import static

from django.urls import re_path
from posts.private_media import ProtectedMediaView

from posts.views import GoogleLogin, ConvertTokenView, UserFeedView, UserProfileView, UploadPhotoView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Added url patterns
    path('api-auth/', include('rest_framework.urls')), # DRF login and logout urls # For testing: http://127.0.0.1:8000/api-auth/login/
    path('posts/', include('posts.urls')),

    # JWT Authentication Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # For media access protection
    re_path(r'^media/(?P<path>.*)$', ProtectedMediaView.as_view(), name='protected_media'),

    # Google OAuth
    path('auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('auth/convert-token/', ConvertTokenView.as_view(), name='convert_token'),

    # Feed endpoint
    path('feed/', UserFeedView.as_view(), name='user-feed'),

    # Profile endpoint
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('upload-photo/', UploadPhotoView.as_view(), name='upload-photo'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
