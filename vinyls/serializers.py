from rest_framework import serializers

from vinyls.models import Genre, Album, Review, CustomUser


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')

    class Meta:
        model = Review
        fields = ['id', 'url', 'album', 'rating', 'content', 'created_at', 'owner']


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    tracks = serializers.StringRelatedField(many=True, read_only=True)
    genres = GenreSerializer(many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Album
        fields = ['id', 'url', 'title', 'artist', 'year', 'genres', 'duration', 'label', 'price', 'tracks', 'reviews']


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'url', 'username', 'reviews']
