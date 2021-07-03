from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from ..models import Files
from filetype.models import Filetype
from .serializer import FilesSerializer
from album.models import Album
from django.core.exceptions import ObjectDoesNotExist
from albumaccess.models import Albumaccess
from album.api.serializer import AlbumSerializers
from django.contrib.auth.models import Group


def changeFile(id):
    try:
        file = Files.objects.get(id=id)
    except ObjectDoesNotExist:
        raise ValidationError('No file found')

    try:
        filetypehidden = Filetype.objects.get(name='Hidden')
    except ObjectDoesNotExist:
        raise ValidationError('No file Type Hidden found')
    try:
        filetypeopen = Filetype.objects.get(name='Open')
    except ObjectDoesNotExist:
        raise ValidationError('No file Type Open found')

    if file.type == filetypehidden:
        file.type = filetypeopen
        file.save()

    elif file.type == filetypeopen:
        file.type = filetypehidden
        file.save()

    serial = FilesSerializer(file,many=False)
    return Response(serial.data)


class ChangeFileAPIView (APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            currentAlbum = Album.objects.get(album_files__id=id)
        except ObjectDoesNotExist:
            raise ValidationError('No Album')

        user = request.user

        if user.is_superuser:
            return changeFile(id)

        elif user.groups.filter(name='Customer').exists():
            return changeFile(id)
        else:
            return Response(False)


def getALLFILES(slug):
    file = Files.objects.filter(album__slug=slug)
    serial = FilesSerializer(file, many=True)
    return Response(serial.data)


def getOPENALLFILES(slug):
    file = Files.objects.filter(album__slug=slug).filter(type__name='Open')
    serial = FilesSerializer(file, many=True)
    return Response(serial.data)


class AlbumFilesAPIView (APIView):
    permission_classes = [AllowAny]

    def get(self, request, slug):
        try:
            currentAlbum = Album.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise ValidationError('No Album')

        try:
            pub_Album = Albumaccess.objects.get(name='Public')
        except ObjectDoesNotExist:
            raise ValidationError('No Album Access')

        try:
            pri_Album = Albumaccess.objects.get(name='Private')
        except ObjectDoesNotExist:
            raise ValidationError('No Album Access')

        if request.user.is_authenticated:
            user = request.user

            if user.is_superuser:
                return getALLFILES(slug)
            else:
                try:
                    accessalbum = Album.objects.get(slug=slug, albumuser_album__user=user)

                    if user.groups.filter(name='Customer').exists():
                        return getALLFILES(slug)
                    elif user.groups.filter(name='Guest').exists():
                        return getOPENALLFILES(slug)
                    else:
                        raise ValidationError('No Access')
                except ObjectDoesNotExist:
                    if currentAlbum.access == pub_Album:
                        return getOPENALLFILES(slug)
                    else:
                        raise ValidationError('No Access')

        else:
            if currentAlbum.access == pub_Album:
                return getOPENALLFILES(slug)
            else:
                raise ValidationError('No Access')


class FilesListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = FilesSerializer
    queryset = Files.objects.all()


class FilesRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = FilesSerializer
    queryset = Files.objects.all()
    lookup_field = 'asset_id'
    lookup_url_kwarg = 'asset_id'


class FilesUpdateAPIView(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = FilesSerializer
    queryset = Files.objects.all()
    lookup_field = 'asset_id'
    lookup_url_kwarg = 'asset_id'


class FilesCreateAPIVIEW(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = FilesSerializer
    queryset = Files.objects.all()
    lookup_field = 'asset_id'
    lookup_url_kwarg = 'asset_id'


class FilesDestoryAPIVIEW(DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = FilesSerializer
    queryset = Files.objects.all()
    lookup_field = 'asset_id'
    lookup_url_kwarg = 'asset_id'
