from rest_framework import serializers
from .models import *

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"




class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=16)
    password = serializers.CharField(max_length=255)