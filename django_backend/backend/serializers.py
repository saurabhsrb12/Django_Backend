from rest_framework import serializers
from .models import Work, Artist
from django.contrib.auth.models import User

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']

class WorkSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True)

    class Meta:
        model = Work
        fields = ['id', 'link', 'work_type', 'artists']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
