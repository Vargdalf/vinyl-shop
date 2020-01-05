from rest_framework import serializers

from vinyls.models import Genre, Album, Review


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True, read_only=True)
    genres = GenreSerializer(many=True)
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # Hyperlink Related Field or serializer

    class Meta:
        model = Album
        fields = ['title', 'artist', 'year', 'genres', 'duration', 'label', 'price', 'tracks', 'reviews']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['rating', 'content', 'created_at']
