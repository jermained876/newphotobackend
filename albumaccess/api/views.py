from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from ..models import Albumaccess
from .serializer import AlbumAccessSerializers


class AlbumAccessDestroyAPIView(DestroyAPIView):
    queryset = Albumaccess.objects.all()
    serializer_class = AlbumAccessSerializers
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'


class AlbumAccessUpdateAPIView(UpdateAPIView):
    queryset = Albumaccess.objects.all()
    serializer_class = AlbumAccessSerializers
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'


class AlbumAccessRetrieveAPIView(RetrieveAPIView):
    queryset = Albumaccess.objects.all()
    serializer_class = AlbumAccessSerializers
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'


class AlbumAccessCreateAPIView(CreateAPIView):
    queryset = Albumaccess.objects.all()
    serializer_class = AlbumAccessSerializers
    permission_classes = [AllowAny]


class AlbumAccessListAPIView(ListAPIView):
    queryset = Albumaccess.objects.all()
    serializer_class = AlbumAccessSerializers
    permission_classes = [AllowAny]


