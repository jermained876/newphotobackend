from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Album
from django.template.defaultfilters import slugify
from albumaccess.api.serializer import AlbumAccessSerializers
from albumuser.models import Albumuser
from django.contrib.auth.models import User, Group

import random


class AlbumCreateSerializers(ModelSerializer):
    id = serializers.CharField(read_only=True)
    slug = serializers.CharField(read_only=True)
    pub_date = serializers.CharField(read_only=True)

    class Meta:
        model = Album
        fields = ['id',
                  'slug',
                  'name',
                  'pub_date',
                  'event_date',
                  'type',
                  'access',
                  ]

    def create(self, validated_data):
        album = Album()
        album.name = validated_data.get('name')
        album.event_date = validated_data.get('event_date')
        album.type = validated_data.get('type')
        album.access = validated_data.get('access')

        slug = slugify('album' + ' ' + str(random.randint(1000, 1000000)))
        check_object = Album.objects.filter(slug=slug)

        while check_object.exists():
            slug = slugify('album' + ' ' + random.randint(1000, 1000000))
            check_object = Album.objects.filter(slug=slug)

        album.slug = slug
        album.save()
        return album


class AlbumSerializers(ModelSerializer):
    id = serializers.CharField(read_only=True)
    slug = serializers.CharField(read_only=True)
    pub_date = serializers.CharField(read_only=True)
    access = AlbumAccessSerializers(many=False)

    class Meta:
        model = Album
        fields = ['id',
                  'slug',
                  'name',
                  'pub_date',
                  'event_date',
                  'type',
                  'access'
                  ]


class AlbumListUserGroupDetailSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields='__all__'


class AlbumListUserDetailSerializer(ModelSerializer):
    groups = AlbumListUserGroupDetailSerializer(many=True)
    
    class Meta:
        model = User
        fields = ['id',
                  'is_superuser',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'groups']


class AlbumListUserSerializer(ModelSerializer):
    user = AlbumListUserDetailSerializer(many=False)

    class Meta:
        model = Albumuser
        fields = ['id',
                  'slug',
                  'album',
                  'user']


class AlbumListSerializers(ModelSerializer):
    id = serializers.CharField(read_only=True)
    slug = serializers.CharField(read_only=True)
    pub_date = serializers.CharField(read_only=True)
    access = AlbumAccessSerializers(many=False)
    albumuser_album = AlbumListUserSerializer(many=True)

    class Meta:
        model = Album
        fields = ['id',
                  'slug',
                  'name',
                  'pub_date',
                  'event_date',
                  'type',
                  'access',
                  'albumuser_album'
                  ]

