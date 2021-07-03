from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView,RetrieveAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Useraccess
from .serializers import UserAccessSerializer
from django.contrib.auth.models import User, Group




class UserAccessCreateAPIView(CreateAPIView):
    queryset = Useraccess.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserAccessSerializer


class UserAccessAllListAPIView(ListAPIView):
    queryset = Useraccess.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserAccessSerializer


class UserAccessRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Useraccess.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserAccessSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


class UserAccessRetrieveAPIView(RetrieveAPIView):
    queryset = Useraccess.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserAccessSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


class UserAccessDestroyAPIView(DestroyAPIView):
    queryset = Useraccess.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserAccessSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
