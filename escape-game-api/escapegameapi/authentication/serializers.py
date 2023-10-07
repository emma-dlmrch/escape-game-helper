from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from authentication.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'],
                                       username=validated_data['username']
                                        )
        user.set_password(validated_data['password'])
        user.save()
        return user