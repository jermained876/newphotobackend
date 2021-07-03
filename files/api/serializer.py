from rest_framework.serializers import ModelSerializer
from ..models import Files
from album.models import Album
from albumaccess.models import Albumaccess
from filetype.models import Filetype
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError


class FilesSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    type = serializers.CharField(read_only=True)

    class Meta:
        model = Files
        fields = [
            'id',
            'album',
            'type',
            'asset_id',
            'bytes',
            'created_at',
            'etag',
            'format',
            'height',
            'original_filename',
            'public_id',
            'resource_type',
            'secure_url',
            'signature',
            'url',
            'width'
        ]

    def create(self, validated_data):

        album = validated_data.get('album')

        try:
            pri_album = Albumaccess.objects.get(name='Private')
            pub_album = Albumaccess.objects.get(name='Public')
        except ObjectDoesNotExist:
            raise ValidationError('No album type found')

        try:
            open_file = Filetype.objects.get(name='Open')
            hidden_file = Filetype.objects.get(name='Hidden')
        except ObjectDoesNotExist:
            raise ValidationError('No File Found')

        new_file = Files()
        new_file.album = album
        new_file.asset_id = validated_data.get('asset_id')
        new_file.bytes = validated_data.get('bytes')
        new_file.created_at = validated_data.get('created_at')
        new_file.etag = validated_data.get('etag')
        new_file.format = validated_data.get('format')
        new_file.height = validated_data.get('height')
        new_file.original_filename = validated_data.get('orginal_filename')
        new_file.public_id = validated_data.get('public_id')
        new_file.resource_type = validated_data.get('resource_type')
        new_file.secure_url = validated_data.get('secure_url')
        new_file.signature = validated_data.get('signature')
        new_file.url = validated_data.get('url')
        new_file.width= validated_data.get('width')


        if album.access == pri_album:
            new_file.type = hidden_file
        elif album.access == pub_album:
            new_file.type = open_file

        new_file.save()
        return new_file