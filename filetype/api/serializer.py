from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Filetype
from django.template.defaultfilters import slugify
import random


class FileTypeSerializer(ModelSerializer):
    id = serializers.CharField(read_only=True)
    slug = serializers.CharField(read_only=True)

    class Meta:
        model = Filetype
        fields = ['id',
                  'slug',
                  'name',
                  ]

    def create(self, validated_data):
        fileType = Filetype()
        fileType.name = validated_data.get('name')

        slug = slugify('filetype' + ' ' + str(random.randint(1000, 1000000)))
        check_object = Filetype.objects.filter(slug=slug)

        while check_object.exists():
            slug = slugify('filetype' + ' ' + random.randint(1000, 1000000))
            check_object = Filetype.objects.filter(slug=slug)

        fileType.slug = slug
        fileType.save()
        return fileType

