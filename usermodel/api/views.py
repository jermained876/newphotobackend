from .serializer import UserCreateSerializer, UserSerializer, UserListSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.response import Response


class UserAllListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserAlbumSearchAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        print(kwargs)

        usernames = User.objects.filter(username__icontains=kwargs.get('username'))
        first_names = User.objects.filter(first_name__icontains=kwargs.get('firstname'))
        last_names = User.objects.filter(last_name__icontains=kwargs.get('lastname'))
        emails = User.objects.filter(email__icontains=kwargs.get('email'))
        albums = User.objects.filter(albumuser_user__album=kwargs.get('album_id'))
        print(kwargs.get('album_id'))
        searchs = set()
        print(len(list(searchs)))
        if usernames.exists():
            if len(list(searchs)) == 0:
                searchs = set(usernames)
                print('tetsing')
            else:
                searchs = searchs.intersection(set(usernames))
                print('tetsing2')
        if first_names.exists():
            if len(list(searchs)) == 0:
                searchs = set(first_names)
            else:
                searchs = searchs.intersection(set(first_names))
        if last_names.exists():
            if len(list(searchs)) == 0:
                searchs = set(last_names)
            else:
                searchs = searchs.intersection(set(last_names))
        if emails.exists():
            if len(list(searchs))== 0:
                searchs = set(emails)
            else:
                searchs = searchs.intersection(set(emails))
        if albums.exists():
            searchs = searchs.difference(set(albums))
            print('Name')

        users = list(searchs)

        #s1.intersection(s2,s3)

        serial = UserListSerializer(users, many=True)
        return Response(serial.data)


class CreateNewUserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer


class CurrentUser(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user = request.user
        serial = UserSerializer(user, many=False)
        return Response(serial.data)



class CurrentUser(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user = request.user
        serial = UserSerializer(user, many=False)
        return Response(serial.data)

