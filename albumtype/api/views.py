from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from ..models import Albumtype
from .serializer import AlbumTypeSerializer


class AlbumTypeDestroyAPIView(DestroyAPIView):
    queryset = Albumtype.objects.all()
    serializer_class = AlbumTypeSerializer
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'


class AlbumTypeUpdateAPIView(UpdateAPIView):
    queryset = Albumtype.objects.all()
    serializer_class = AlbumTypeSerializer
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'


class AlbumTypeRetrieveAPIView(RetrieveAPIView):
    queryset = Albumtype.objects.all()
    serializer_class = AlbumTypeSerializer
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'


class AlbumTypeCreateAPIView(CreateAPIView):
    queryset = Albumtype.objects.all()
    serializer_class = AlbumTypeSerializer
    permission_classes = [AllowAny]


class AlbumTypeListAPIView(ListAPIView):
    queryset = Albumtype.objects.all()
    serializer_class = AlbumTypeSerializer
    permission_classes = [AllowAny]


