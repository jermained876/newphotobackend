from rest_framework.generics import CreateAPIView,ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView, RetrieveDestroyAPIView
from ..models import Carousel
from .serializer import CarouselSerializer
from rest_framework.permissions import AllowAny


class CarouselRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer
    lookup_url_kwarg = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [AllowAny]


class CarouselRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer
    lookup_url_kwarg = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [AllowAny]


class CarouselRetrieveAPIView(RetrieveAPIView):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer
    lookup_url_kwarg = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = [AllowAny]


class CarouselCreateAPIView(CreateAPIView):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer
    permission_classes = [AllowAny]


class CarouselListAPIView(ListAPIView):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer
    permission_classes = [AllowAny]

