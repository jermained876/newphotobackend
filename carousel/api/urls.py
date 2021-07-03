from django.urls import path
from .views import CarouselCreateAPIView, CarouselListAPIView, CarouselRetrieveAPIView, CarouselRetrieveDestroyAPIView, CarouselRetrieveUpdateAPIView


urlpatterns = [
    path('/all', CarouselListAPIView.as_view(), name='all'),
    path('/create', CarouselCreateAPIView.as_view(), name='create'),
    path('/<str:id>', CarouselRetrieveAPIView.as_view(), name='detail'),
    path('/<str:id>/edit', CarouselRetrieveUpdateAPIView.as_view(), name='update'),
    path('/<str:id>/delete', CarouselRetrieveDestroyAPIView.as_view(), name='delete'),
]
