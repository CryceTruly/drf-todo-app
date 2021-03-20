from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email','token','username','is_verified', 'password']
        read_only_fields = ['token','is_verified']
