from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from album.api.serializer import AlbumSerializers
from django.contrib.auth.models import User
from album.models import Album
from albumtype.models import Albumtype
from albumaccess.models import Albumaccess
from albumuser.models import Albumuser
from gift.models import Gift
from albumuser.api.serializer import AlbumUsersSerializers
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError
from files.models import Files
from files.api.serializer import FilesSerializer
from albumaccess.models import Albumaccess
from useraccess.api.serializers import UserAccessSerializer
from useraccess.models import Useraccess
from .serializer import UserListSerializer, UserCreateSerializer


class UserCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = 'id'
    lookup_field = 'id'


class UserAllListAPIView (ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserListSerializer
    queryset = User.objects.all()


class getAlbumFiles(APIView):
    permission_classes = [AllowAny]

    def get(self, request, slug):
        name ='start'
        current_user = request.user

        try:
            # get if member as access to the album
            album1 = Album.objects.get(slug=slug, albumuser_album__user=current_user)
            serial = AlbumSerializers(album1, many=False)

            # get user access type

            try:
                # get user type
                type = Useraccess.objects.get(user=request.user)
                serial1 = UserAccessSerializer(type, many=False)
            except ObjectDoesNotExist:
                user = 'null'

        except ObjectDoesNotExist:
            raise ValidationError("Album don't exist")

        #find files based on user access level
        access_name = type.role.name
        if (access_name=='Customer'):
            name = 'Customer'
            album_files = Files.objects.filter(album__slug=slug)
        if (access_name=='Guest'):
            name ='Guest'
            album_files = Files.objects.filter(album__slug=slug).filter(type__name='Open')

        serial2=FilesSerializer(album_files, many=True)

        return Response(serial2.data)


class getPrivateAlbumAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        album = Album.objects.filter(albumuser_album__user=user)
        serial = AlbumSerializers(album, many=True)
        return Response(serial.data)


class getPublicAlbumAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        albumAccess = Albumaccess.objects.get(name='Public')
        publicAlbum = Album.objects.filter(access=albumAccess)
        serial = AlbumSerializers(publicAlbum, many=True)
        return Response(serial.data)


class getPublicAlbumCategoryAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, slug):
        albumAccess = Albumaccess.objects.get(name='Public')
        albumtype = Albumtype.objects.get(slug=slug)
        publicAlbum = Album.objects.filter(type=albumtype, access=albumAccess)
        serial = AlbumSerializers(publicAlbum, many=True)
        return Response(serial.data)





#class CurrentUser(APIView):
 #   permission_classes = [AllowAny]

  #  def get(self, request):
   #     user = request.user
   #     serial = UserSerializer(user, many=False)
    #    return Response(serial.data)


