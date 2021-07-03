from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Albumuser
from django.template.defaultfilters import slugify
from rest_framework.exceptions import ValidationError
import random
from django.core.exceptions import ObjectDoesNotExist
from album.api.serializer import AlbumSerializers
from userapi.api.serializer import AlbumSerializer


class AlbumUsersSerializers(ModelSerializer):
    id = serializers.CharField(read_only=True)
    slug = serializers.CharField(read_only=True)

    class Meta:
        model = Albumuser
        fields = ['id',
                  'slug',
                  'album',
                  'user',
                  ]

    def create(self, validated_data):
        try:
            a = validated_data.get('album')
            u = validated_data.get('user')
            objC = Albumuser.objects.get(album=a, user=u)
            raise ValidationError('Access already exist')

        except ObjectDoesNotExist:
            albumusers = Albumuser()
            albumusers.album = validated_data.get('album')
            albumusers.user = validated_data.get('user')

            slug = slugify('albumuser' + ' ' + str(random.randint(1000, 1000000)))
            check_object = Albumuser.objects.filter(slug=slug)

            while check_object.exists():
                slug = slugify('albumuser' + ' ' + random.randint(1000, 1000000))
                check_object = Albumuser.objects.filter(slug=slug)

            albumusers.slug = slug
            albumusers.save()
            return albumusers



class AlbumListUsersSerializers(ModelSerializer):

    class Meta:
        model = Albumuser
        fields = ['id',
                  'slug',
                  'album',
                  'user',
                  ]