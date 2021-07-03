

from django.urls import path
from .views import UserAccessCreateAPIView, UserAccessAllListAPIView, UserAccessRetrieveAPIView, UserAccessDestroyAPIView, UserAccessRetrieveUpdateAPIView

urlpatterns = [
    path('/all', UserAccessAllListAPIView.as_view(), name='all'),
    path('/create', UserAccessCreateAPIView.as_view(), name='create'),
    path('/<str:slug>', UserAccessRetrieveAPIView.as_view(), name='detail'),
    path('/<str:slug>/edit', UserAccessRetrieveUpdateAPIView.as_view(), name='update'),
    path('/<str:slug>/delete', UserAccessDestroyAPIView.as_view(), name='delete'),
   ]
