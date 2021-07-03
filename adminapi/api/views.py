from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth.models import User, Group
from rest_framework.permissions import AllowAny, IsAdminUser , IsAuthenticated
from .serializer import UserInfoSerializer, CreateCustomerUserSerializer, CreateGuestUserSerializer, CreateCustomerInfoSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from album.models import Album
from albumaccess.models import Albumaccess
from album.api.serializer import AlbumSerializers
from files.models import Files
from files.api.serializer import FilesSerializer
from filetype.models import Filetype


class AdminAccessOnlyAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response(True)


class AuthenticatedAccessOnlyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(True)

def getOwnerFiles(slug):
    album_files = Files.objects.filter(album__slug=slug)
    serial = FilesSerializer(album_files, many=True)
    return Response(serial.data)


class GetAlbumFilesAuthAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, slug):
        user = request.user
        #check is file exist
        try:
            album1 = Album.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise ValidationError('Album does not exist')
        #check if user is admin

        if user.is_superuser:
            return  getOwnerFiles(slug)
        else:
            #check if user as Customer access
            if user.groups.filter(name='Customer').exists():
                #check if user has access to album
                try:
                    access = Album.objects.get(album_files__asset_id=slug, albumuser_album__user=user)
                    return  getOwnerFiles(slug)
                except ObjectDoesNotExist:
                    raise ValidationError('No Access')
            else:
                album_files = Files.objects.filter(album__slug=slug).filter(type__name='Open')
                serial = FilesSerializer(album_files,many=True)
                return Response(serial.data)


class GetCurrentUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serial = UserInfoSerializer(user,many=False)
        return Response(serial.data)


def changeToHidden(slug):
    try:
        currentfile = Files.objects.get(asset_id=slug)
    except ObjectDoesNotExist:
        raise ValidationError('File does not exist')

    try:
        filetype = Filetype.objects.get(name='Hidden')
        currentfile.type = filetype
        currentfile.save()
        serial = FilesSerializer(currentfile, many=False)
        return Response(serial.data)
    except ObjectDoesNotExist:
        raise ValidationError('File open dont exist')


class ChangeFileToHidden(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, slug):
        user = request.user
        #check is file exist
        try:
            currentfile = Files.objects.get(asset_id=slug)
        except ObjectDoesNotExist:
            raise ValidationError('File does not exist')
        #check if user is admin
        if user.is_superuser:
            return changeToHidden(slug)
        else:
            #check if user as Customer access
            if user.groups.filter(name='Customer').exists():
                #check if user has access to album
                try:
                    access = Album.objects.get(album_files__asset_id=slug, albumuser_album__user=user)
                    return changeToHidden(slug)
                except ObjectDoesNotExist:
                    raise ValidationError('No Access')
            else:
                raise ValidationError('No Acccess')


def changeToOpen(slug):
    try:
        currentfile = Files.objects.get(asset_id=slug)
    except ObjectDoesNotExist:
        raise ValidationError('File does not exist')

    try:
        filetype = Filetype.objects.get(name='Open')
        currentfile.type = filetype
        currentfile.save()
        serial = FilesSerializer(currentfile, many=False)
        return Response(serial.data)
    except ObjectDoesNotExist:
        raise ValidationError('File open dont exist')


class ChangeFileToOpen(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, slug):
        user = request.user
        #check is file exist
        try:
            currentfile = Files.objects.get(asset_id=slug)
        except ObjectDoesNotExist:
            raise ValidationError('File does not exist')
        #check if user is admin
        if user.is_superuser:
            return changeToOpen(slug)
        else:
            #check if user as Customer access
            if user.groups.filter(name='Customer').exists():
                #check if user has access to album
                try:
                    access = Album.objects.get(album_files__asset_id=slug, albumuser_album__user=user)
                    return changeToOpen(slug)
                except ObjectDoesNotExist:
                    raise ValidationError('No Access')
            else:
                raise ValidationError('No Acccess')


class AlbumToPublicAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, slug):

        try:
            album = Album.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise ValidationError('Album does not exist')
        #check if user is admin

        try:
            albumPublic = Albumaccess.objects.get(name='Public')
            album.access = albumPublic
            album.save()
            files = Files.objects.filter(album__slug=slug)

            try:
                filetypehidden = Filetype.objects.get(name='Open')
            except ObjectDoesNotExist:
                raise ValidationError('No file Type Hidden found')

            if files.exists():
                for file in files:
                    file.type = filetypehidden
                    file.save()

            serial = FilesSerializer(files, many=True)
            return Response(serial.data)
        except ObjectDoesNotExist:
            raise ValidationError('No Access')


class AlbumToPrivatAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, slug):

        try:
            album = Album.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise ValidationError('Album does not exist')
        #check if user is admin

        try:
            albumPublic = Albumaccess.objects.get(name='Private')
            album.access = albumPublic
            album.save()
            files = Files.objects.filter(album__slug=slug)

            try:
                filetypehidden = Filetype.objects.get(name='Hidden')
            except ObjectDoesNotExist:
                raise ValidationError('No file Type Hidden found')

            if files.exists():
                for file in files:
                    file.type = filetypehidden
                    file.save()

            serial = FilesSerializer(files, many=True)
            return Response(serial.data)
        except ObjectDoesNotExist:
            raise ValidationError('No Access')


class ReUSeCode(APIView):
    permission_classes = [AllowAny]

    def get(self,request, slug):
        user = request.user
        #get the album
        try:
            album = Album.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise ValidationError('Album does not exist')
        #check if user is admin
        if user.is_superuser:
            try:
                albumPublic = Albumaccess.objects.get(name='Private')
                album.access = albumPublic
                album.save()
                files = Files.objects.filter(album__slug=slug)

                try:
                    filetypehidden = Filetype.objects.get(name='Hidden')
                except ObjectDoesNotExist:
                    raise ValidationError('No file Type Hidden found')

                if files.exists():
                    for file in files:
                        file.type = filetypehidden
                        file.save()

                serial = FilesSerializer(files, many=True)
                return Response(serial.data)
            except ObjectDoesNotExist:
                raise ValidationError('No Access')
        else:
            #check if user as Customer access
            if user.groups.filter(name='Customer').exists():
                #check if user has access to album
                try:
                    access = Album.objects.get(slug=slug, albumuser_album__user=user)
                    try:
                        albumPublic = Albumaccess.objects.get(name='Private')
                        album.access = albumPublic
                        album.save()
                        files = Files.objects.filter(album__slug=slug)

                        try:
                            filetypehidden = Filetype.objects.get(name='Hidden')
                        except ObjectDoesNotExist:
                            raise ValidationError('No file Type Hidden found')

                        if files.exists():
                            for file in files:
                                file.type = filetypehidden
                                file.save()

                        serial = FilesSerializer(files, many=True)
                        return Response(serial.data)
                    except ObjectDoesNotExist:
                        raise ValidationError('No Access')
                except ObjectDoesNotExist:
                    raise ValidationError('No Access')
            else:
                raise ValidationError('No Acccess')


class ChangeToAdminAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, username):
        user = User.objects.get(username=username)
        #remove admin settings
        user.is_superuser = True
        user.is_staff = True
        user.save()

        # Find Customer Group

        user.groups.clear()

        serial = CreateCustomerInfoSerializer(user, many=False)
        return Response(serial.data)


class ChangeToGuestAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, username):
        user = User.objects.get(username=username)
        #remove admin settings
        user.is_superuser = False
        user.is_staff = False
        user.save()

        # Find Customer Group
        try:
            group = Group.objects.get(name='Guest')
            user.groups.set([group])
        except ObjectDoesNotExist:
            raise ValidationError('Group do not exist')
        serial = CreateCustomerInfoSerializer(user, many=False)
        return Response(serial.data)


class ChangeToCustomerAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, username):
        user = User.objects.get(username=username)
        #remove admin settings
        user.is_superuser = False
        user.is_staff = False
        user.save()

        # Find Customer Group
        try:
            group = Group.objects.get(name='Customer')
            user.groups.set([group])
        except ObjectDoesNotExist:
            raise ValidationError('Group do not exist')
        serial = CreateCustomerInfoSerializer(user, many=False)
        return Response(serial.data)


class CreateGuestUserCreateAPIView(CreateAPIView):
    serializer_class = CreateGuestUserSerializer
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()


class CreateCustomerUserCreateAPIView(CreateAPIView):
    serializer_class = CreateCustomerUserSerializer
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()


