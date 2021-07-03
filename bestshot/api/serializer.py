from rest_framework.serializers import ModelSerializer
from bestshot.models import Bestshot


class BestshotSerializer(ModelSerializer):
    class Meta:
        model = Bestshot
        fields ='__all__'
