from rest_framework import serializers
from .models import Artist, Track
from django.contrib.auth.models import User, Group


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    tracks = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='track-detail'  # Имя представления для деталей трека
    )

    class Meta:
        model = Artist
        fields = ['url', 'id', 'name', 'bio', 'tracks']

class TrackSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist-detail',  # Имя представления для деталей исполнителя
        read_only=True
    )

    class Meta:
        model = Track
        fields = ['url', 'id', 'title', 'artist', 'album', 'genre', 'duration', 'release_date']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']