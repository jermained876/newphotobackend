from rest_framework.serializers import ModelSerializer
from ..models import Accesstype


class AccessTypeSerializer(ModelSerializer):
    class Meta:
        model = Accesstype
        fields= [ 'id',
                  'name',
                  'slug']