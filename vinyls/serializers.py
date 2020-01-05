from django.contrib.auth.models import User
from rest_framework import serializers

from vinyls.models import Genre, Album, Review


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = ['id', 'album', 'url', 'rating', 'content', 'created_at', 'owner']


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    tracks = serializers.StringRelatedField(many=True, read_only=True)
    genres = GenreSerializer(many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Album
        fields = ['id', 'url', 'title', 'artist', 'year', 'genres', 'duration', 'label', 'price', 'tracks', 'reviews']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.PrimaryKeyRelatedField(many=True, queryset=Review.objects.all())

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'reviews']
