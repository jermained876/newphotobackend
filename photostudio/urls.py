"""photostudio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accesstype', include('accesstype.api.urls')),
    path('api/user', include('usermodel.api.urls')),
    path('api/useraccess', include('useraccess.api.urls')),
    path('api/albumtype', include('albumtype.api.urls')),
    path('api/albumaccess', include('albumaccess.api.urls')),
    path('api/album', include('album.api.urls')),
    path('api/albumuser', include('albumuser.api.urls')),
    path('api/userapi', include('userapi.api.urls')),
    path('api/adminapi', include('adminapi.api.urls')),
    path('api/bestshot', include('bestshot.api.urls')),
    path('api/carousel', include('carousel.api.urls')),
    path('api/file', include('files.api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
