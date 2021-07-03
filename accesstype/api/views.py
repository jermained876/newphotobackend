from rest_framework.generics import ListAPIView
from .serializer import AccessTypeSerializer
from rest_framework.permissions import AllowAny
from ..models import Accesstype


class AccesstypeListAPIView(ListAPIView):
    queryset = Accesstype.objects.all()
    permission_classes = [AllowAny]
    serializer_class = AccessTypeSerializer