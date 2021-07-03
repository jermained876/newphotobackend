from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from ..models import Album
from .serializer import AlbumSerializers, AlbumCreateSerializers, AlbumListSerializers
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError
from albumaccess.models import Albumaccess
from rest_framework.response import Response
from albumuser.models import Albumuser
from django.contrib.auth.models import AnonymousUser, User


class UserAlbumsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.is_superuser:
            albums = Album.objects.all()
            serial = AlbumSerializers(albums, many=True)
            return Response(serial.data)

        else:
            albums = Album.objects.filter(albumuser_album__user=user)
            serial = AlbumSerializers(albums, many=True)
            return Response(serial.data)


class AlbumVisibleControlAPIView (APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, slug):
        try:
            currentAlbum = Album.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise ValidationError('No Album')

        user = request.user

        if user.is_superuser:
            return Response(True)

        elif user.groups.filter(name='Customer').exists():
            return Response(True)
        else:
            return Response(False)


class AlbumAccessAPIView (APIView):
    permission_classes = [AllowAny]

    def get(self, request, slug):
        try:
            currentAlbum = Album.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise ValidationError('No Album')

        try:
            pub_Album = Albumaccess.objects.get(name='Public')
        except ObjectDoesNotExist:
            raise ValidationError('No Album')

        try:
            pri_Album = Albumaccess.objects.get(name='Private')
        except ObjectDoesNotExist:
            raise ValidationError('No Album')

        if currentAlbum.access == pub_Album:
            serial = AlbumSerializers(currentAlbum, many=False)
            return Response(serial.data)

        if currentAlbum.access == pri_Album:
            if request.user.is_authenticated:
                user = request.user
                if(user.is_superuser):
                    try:
                        accessalbum = Album.objects.get(slug=slug)
                        serial = AlbumSerializers(accessalbum, many=False)
                        return Response(serial.data)
                    except ObjectDoesNotExist:
                        raise ValidationError('No Album3')
                try:

                    accessalbum = Album.objects.get(slug=slug, albumuser_album__user=user)
                    serial = AlbumSerializers(accessalbum, many=False)
                    return Response(serial.data)
                except ObjectDoesNotExist:
                    raise ValidationError('No Access4')
            else:
                raise ValidationError('No Access5')


class AlbumDestroyAPIView(DestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'


class AlbumUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumCreateSerializers
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'id'
    lookup_field = 'id'


class AlbumRetrieveAPIView(RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'


class AlbumCreateAPIView(CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumCreateSerializers
    permission_classes = [AllowAny]


class AlbumListAPIView(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumListSerializers
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ['name']


