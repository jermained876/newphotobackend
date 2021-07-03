from django.contrib.auth.models import User, Group
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from albumuser.models import Albumuser
from album.models import Album


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class AlbumUserSerializer(ModelSerializer):
    album = AlbumSerializer(many=False)

    class Meta:
        model = Albumuser
        fields = ['id','album']


class GroupSerializer (ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class UserListSerializer (ModelSerializer):
    groups = GroupSerializer(many=True)
    albumuser_user = AlbumUserSerializer(many=True)

    class Meta:
        model = User
        fields = ['id','username','is_superuser','first_name','last_name', 'email', 'groups','albumuser_user']


class UserCreateSerializer (ModelSerializer):
    access = serializers.CharField(write_only=True)
    is_superuser = serializers.CharField(read_only=True)
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','is_superuser','groups', 'email', 'access']

    def create(self, validated_data):
        new_user = User()
        new_user.username = validated_data.get('username')
        new_user.first_name = validated_data.get('first_name')
        new_user.last_name = validated_data.get('last_name')
        new_user.email = validated_data.get('email')
        new_user.set_password('Password@123')

        access = validated_data.get('access')
        if access == 'Admin':
            new_user.is_superuser = True
            new_user.is_staff = True
        new_user.save()

        if access == 'Customer':
            try:
                group = Group.objects.get(name='Customer')
                new_user.groups.set([group])
            except ObjectDoesNotExist:
                raise ValidationError('Group do not exist')
        elif access == 'Guest':
            try:
                group = Group.objects.get(name='Guest')
                new_user.groups.set([group])
            except ObjectDoesNotExist:
                raise ValidationError('Group do not exist')

        return new_user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username')
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.email = validated_data.get('email')
        access = validated_data.get('access')

        if access == 'Admin':
            instance.is_superuser = True
            instance.is_staff = True
        else:
            instance.is_superuser = False
            instance.is_staff = False
        instance.save()

        instance.groups.clear()
        if access == 'Customer':
            try:
                group = Group.objects.get(name='Customer')
                instance.groups.set([group])
            except ObjectDoesNotExist:
                raise ValidationError('Group do not exist')
        elif access == 'Guest':
            try:
                group = Group.objects.get(name='Guest')
                instance.groups.set([group])
            except ObjectDoesNotExist:
                raise ValidationError('Group do not exist')

        return instance
