from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from ..models import Bestshot
from .serializer import BestshotSerializer
from rest_framework.permissions import AllowAny


class BestshotCreateAPIView(CreateAPIView):
    serializer_class = BestshotSerializer
    queryset = Bestshot.objects.all()
    permission_classes = [AllowAny]


class BestshotRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = BestshotSerializer
    queryset = Bestshot.objects.all()
    lookup_url_kwarg = 'id'
    lookup_field = 'id'
    permission_classes = [AllowAny]


class BestshotRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = BestshotSerializer
    queryset = Bestshot.objects.all()
    lookup_url_kwarg = 'id'
    lookup_field = 'id'
    permission_classes = [AllowAny]


class BestshotRetrieveAPIView(RetrieveAPIView):
    serializer_class = BestshotSerializer
    queryset = Bestshot.objects.all()
    lookup_url_kwarg = 'id'
    lookup_field = 'id'
    permission_classes = [AllowAny]


class BestshotListAPIView(ListAPIView):
    serializer_class = BestshotSerializer
    queryset = Bestshot.objects.all()
    permission_classes = [AllowAny]