from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from ..models import Albumuser
from .serializer import AlbumUsersSerializers


class AlbumUsersDestroyAPIView(DestroyAPIView):
    queryset = Albumuser.objects.all()
    serializer_class = AlbumUsersSerializers
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'id'
    lookup_field = 'id'


class AlbumUsersUpdateAPIView(UpdateAPIView):
    queryset = Albumuser.objects.all()
    serializer_class = AlbumUsersSerializers
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'id'
    lookup_field = 'id'


class AlbumUsersRetrieveAPIView(RetrieveAPIView):
    queryset = Albumuser.objects.all()
    serializer_class = AlbumUsersSerializers
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'id'
    lookup_field = 'id'


class AlbumUsersCreateAPIView(CreateAPIView):
    queryset = Albumuser.objects.all()
    serializer_class = AlbumUsersSerializers
    permission_classes = [AllowAny]


class AlbumUsersListAPIView(ListAPIView):
    queryset = Albumuser.objects.all()
    serializer_class = AlbumUsersSerializers
    permission_classes = [AllowAny]


