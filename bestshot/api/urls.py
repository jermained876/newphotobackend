from django.urls import path
from .views import BestshotCreateAPIView, BestshotListAPIView,BestshotRetrieveAPIView,BestshotRetrieveDestroyAPIView,BestshotRetrieveUpdateAPIView

urlpatterns = [
    path('/all', BestshotListAPIView.as_view(), name='all'),
    path('/create', BestshotCreateAPIView.as_view(), name='create'),
    path('/<str:id>', BestshotRetrieveAPIView.as_view(), name='detail'),
    path('/<str:id>/edit', BestshotRetrieveUpdateAPIView.as_view(), name='update'),
    path('/<str:id>/delete', BestshotRetrieveDestroyAPIView.as_view(), name='delete'),
]
