

from django.urls import path
from .views import UserUpdateAPIView, UserCreateAPIView,UserAllListAPIView, getPublicAlbumAPIView, getPublicAlbumCategoryAPIView, getPrivateAlbumAPIView, getAlbumFiles

urlpatterns = [
    path('/all', UserAllListAPIView.as_view(), name='allusers'),
    path('/create', UserCreateAPIView.as_view(), name='create'),
    path('/<str:id>/update', UserUpdateAPIView.as_view(), name='update'),
    path('/allPublicAlbums', getPublicAlbumAPIView.as_view(), name='allPublic'),
    path('/allPublicAlbumsCategory/<str:slug>/', getPublicAlbumCategoryAPIView.as_view(), name='allPublicCategory'),
    path('/allPrivateAlbums', getPrivateAlbumAPIView.as_view(), name='allPrivate'),
    path('/allAlbumFiles/<str:slug>/', getAlbumFiles.as_view(), name='allAlbumFiles'),

]
