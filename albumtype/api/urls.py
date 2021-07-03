

from django.urls import path
from .views import AlbumTypeListAPIView, AlbumTypeCreateAPIView, AlbumTypeRetrieveAPIView, AlbumTypeUpdateAPIView, AlbumTypeDestroyAPIView

urlpatterns = [
    path('/all', AlbumTypeListAPIView.as_view(), name='all'),
    path('/create', AlbumTypeCreateAPIView.as_view(), name='create'),
    path('/<str:slug>', AlbumTypeRetrieveAPIView.as_view(), name='detail'),
    path('/<str:slug>/edit', AlbumTypeUpdateAPIView.as_view(), name='update'),
    path('/<str:slug>/delete', AlbumTypeDestroyAPIView.as_view(), name='delete'),
]
