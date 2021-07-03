from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from ..models import Filetype
from .serializer import FileTypeSerializer


class FileTypeDestroyAPIView(DestroyAPIView):
    queryset = Filetype.objects.all()
    serializer_class = FileTypeSerializer
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'


class FileTypeUpdateAPIView(UpdateAPIView):
    queryset = Filetype.objects.all()
    serializer_class = FileTypeSerializer
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'


class FileTypeRetrieveAPIView(RetrieveAPIView):
    queryset = Filetype.objects.all()
    serializer_class = FileTypeSerializer
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'


class FileTypeCreateAPIView(CreateAPIView):
    queryset = Filetype.objects.all()
    serializer_class = FileTypeSerializer
    permission_classes = [AllowAny]


class FileTypeListAPIView(ListAPIView):
    queryset = Filetype.objects.all()
    serializer_class = FileTypeSerializer
    permission_classes = [AllowAny]


