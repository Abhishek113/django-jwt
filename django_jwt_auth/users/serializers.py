from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    data_joined = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'data_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}