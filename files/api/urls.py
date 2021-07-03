

from django.urls import path
from .views import ChangeFileAPIView,AlbumFilesAPIView, FilesCreateAPIVIEW, FilesRetrieveAPIView, FilesListAPIView, FilesDestoryAPIVIEW, FilesUpdateAPIView

urlpatterns = [
    path('/all', FilesListAPIView.as_view(), name='all'),
    path('/create', FilesCreateAPIVIEW.as_view(), name='create'),
    path('/<str:slug>', FilesRetrieveAPIView.as_view(), name='detail'),
    path('/<str:slug>/edit', FilesUpdateAPIView.as_view(), name='update'),
    path('/<str:slug>/delete', FilesDestoryAPIVIEW.as_view(), name='delete'),
    path('/albumfiles/<str:slug>/', AlbumFilesAPIView.as_view(), name='delete'),
    path('/changeFile/<str:id>/', ChangeFileAPIView.as_view(), name='delete'),

]
