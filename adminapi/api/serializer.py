from django.contrib.auth.models import Group, User
from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from django.template.defaultfilters import slugify
from django.template.defaultfilters import slugify
import random


class GroupInfoSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = ['name']


class CreateCustomerInfoSerializer(ModelSerializer):
    groups = GroupInfoSerializer(many=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'groups', 'is_superuser', 'is_staff']


class UserInfoSerializer(ModelSerializer):
    groups = GroupInfoSerializer(many=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'groups', 'is_superuser', 'is_staff']


class CreateGuestUserSerializer(ModelSerializer):
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        try:
            group = Group.objects.get(name='Guest')
        except ObjectDoesNotExist:
            raise ValidationError('Group does not exist')

        user = User()
        user.username = slugify('Guest ' + str(random.randint(1000, 100000)))
        user.set_password('Windows@123')
        user.is_superuser
        user.is_staff
        user.save()
        user.groups.set([group])

        return user


class CreateCustomerUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        try:
            group = Group.objects.get(name='Customer')
        except ObjectDoesNotExist:
            raise ValidationError('Group does not exist')

        user = User()
        user.username = validated_data.get('username')
        user.email = validated_data.get('email')
        user.first_name = validated_data.get('first_name')
        user.last_name = validated_data.get('last_name')
        user.set_password(validated_data.get('password'))
        user.save()
        user.groups.set([group])

        return user






