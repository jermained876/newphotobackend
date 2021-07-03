from django.urls import path
from .views import UserAllListAPIView, UserAlbumSearchAPIView, CreateNewUserCreateAPIView, CurrentUser

urlpatterns = [
    path('/create', CreateNewUserCreateAPIView.as_view(), name='create'),
    path('/all', UserAllListAPIView.as_view(), name='all'),
    path('/current', CurrentUser.as_view(), name='current'),
    path('/searchAlbumUsers/<str:album_id>/<str:username>/<str:firstname>/<str:lastname>/<str:email>', UserAlbumSearchAPIView.as_view(), name='detail'),

]
