from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'email', 'is_staff', 'avatar', 'first_name', 'last_name']
