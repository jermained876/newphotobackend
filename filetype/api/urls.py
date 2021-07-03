

from django.urls import path
from .views import FileTypeCreateAPIView, FileTypeListAPIView, FileTypeDestroyAPIView, FileTypeUpdateAPIView, FileTypeRetrieveAPIView

urlpatterns = [
    path('/all', FileTypeListAPIView.as_view(), name='all'),
    path('/create', FileTypeCreateAPIView.as_view(), name='create'),
    path('/<str:slug>', FileTypeRetrieveAPIView.as_view(), name='detail'),
    path('/<str:slug>/edit', FileTypeUpdateAPIView.as_view(), name='update'),
    path('/<str:slug>/delete', FileTypeDestroyAPIView.as_view(), name='delete'),
]
