from django.contrib.auth.models import User, Group
from rest_framework.serializers import ModelSerializer


class GroupsSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class UserListSerializer(ModelSerializer):
    groups = GroupsSerializer(many=True)
    class Meta:
        model = User
        fields = ['id',
                  'is_superuser',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'groups',
                  ]


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password'
                  ]


class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password'
                  ]

    def create(self, validated_data):
        newUser = User()
        newUser.username = validated_data.get('username')
        newUser.first_name = validated_data.get('first_name')
        newUser.last_name = validated_data.get('last_name')
        newUser.email = validated_data.get('email')
        newUser.set_password(validated_data.get('password'))
        newUser.save()
        return newUser
