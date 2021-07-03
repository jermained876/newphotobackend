from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Albumtype
from django.template.defaultfilters import slugify
import random


class AlbumTypeSerializer(ModelSerializer):
    id = serializers.CharField(read_only=True)
    slug = serializers.CharField(read_only=True)

    class Meta:
        model = Albumtype
        fields = ['id',
                 'slug',
                 'name',
                  ]

    def create(self, validated_data):
        albumType = Albumtype()
        albumType.name = validated_data.get('name')

        slug = slugify('albumtype' + ' ' + str(random.randint(1000, 1000000)))
        check_object = Albumtype.objects.filter(slug=slug)

        while check_object.exists():
            slug = slugify('albumtype' + ' ' + random.randint(1000, 1000000))
            check_object = Albumtype.objects.filter(slug=slug)
        
        albumType.slug = slug
        albumType.save()
        return albumType

