from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Useraccess
from usermodel.api.serializer import UserCreateSerializer
from accesstype.api.serializer import AccessTypeSerializer
from django.template.defaultfilters import slugify
import random


class UserAccessSerializer(ModelSerializer):
    slug = serializers.CharField(read_only=True)
    user = UserCreateSerializer(many=False)
    role = AccessTypeSerializer(many=False)

    class Meta:
        model = Useraccess
        fields = ['id',
                  'slug',
                  'user',
                  'role']

    def create(self, validated_data):
        userAc = Useraccess()
        userAc.user = validated_data.get('user')
        userAc.role = validated_data.get('role')

        slug = slugify('useracess' + ' ' + str(random.randint(1000, 1000000)))
        check_object = Useraccess.objects.filter(slug=slug)

        while check_object.exists():
            slug = slugify('useracess' + ' ' + random.randint(1000, 1000000))
            check_object = Useraccess.objects.filter(slug=slug)

        userAc.slug = slug

        userAc.save()
        return userAc