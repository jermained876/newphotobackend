

from django.urls import path
from .views import AlbumAccessListAPIView, AlbumAccessCreateAPIView, AlbumAccessDestroyAPIView, AlbumAccessRetrieveAPIView, AlbumAccessUpdateAPIView

urlpatterns = [
    path('/all', AlbumAccessListAPIView.as_view(), name='all'),
    path('/create', AlbumAccessCreateAPIView.as_view(), name='create'),
    path('/<str:slug>', AlbumAccessRetrieveAPIView.as_view(), name='detail'),
    path('/<str:slug>/edit', AlbumAccessUpdateAPIView.as_view(), name='update'),
    path('/<str:slug>/delete', AlbumAccessDestroyAPIView.as_view(), name='delete'),
]
