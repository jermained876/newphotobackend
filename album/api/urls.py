

from django.urls import path
from .views import UserAlbumsAPIView, AlbumVisibleControlAPIView, AlbumAccessAPIView, AlbumCreateAPIView, AlbumListAPIView, AlbumDestroyAPIView, AlbumRetrieveAPIView, AlbumUpdateAPIView

urlpatterns = [
    path('/userAlbum', UserAlbumsAPIView.as_view(), name='userAlbum'),
    path('/all', AlbumListAPIView.as_view(), name='all'),
    path('/create', AlbumCreateAPIView.as_view(), name='create'),
    path('/<str:slug>', AlbumRetrieveAPIView.as_view(), name='detail'),
    path('/<str:id>/edit', AlbumUpdateAPIView.as_view(), name='update'),
    path('/<str:slug>/delete', AlbumDestroyAPIView.as_view(), name='delete'),
    path('/albumAccess/<str:slug>', AlbumAccessAPIView.as_view(), name='delete'),
    path('/albumVisibleControl/<str:slug>', AlbumVisibleControlAPIView.as_view(), name='VisibleControl'),

]
