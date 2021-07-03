

from django.urls import path
from .views import AlbumUsersCreateAPIView, AlbumUsersDestroyAPIView, AlbumUsersListAPIView, AlbumUsersRetrieveAPIView, AlbumUsersUpdateAPIView

urlpatterns = [
    path('/all', AlbumUsersListAPIView.as_view(), name='all'),
    path('/create', AlbumUsersCreateAPIView.as_view(), name='create'),
    path('/<str:id>', AlbumUsersRetrieveAPIView.as_view(), name='detail'),
    path('/<str:slug>/edit', AlbumUsersUpdateAPIView.as_view(), name='update'),
    path('/<str:id>/delete', AlbumUsersDestroyAPIView.as_view(), name='delete'),
]
