from rest_framework import serializers

from vinyls.models import Genre, Album, Review, CustomUser, ShoppingCart, ShoppingCartItem


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(read_only=True, view_name='customuser-detail')

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


class ShoppingCartItemSerializer(serializers.HyperlinkedModelSerializer):
    album = AlbumSerializer()

    class Meta:
        model = ShoppingCartItem
        fields = ['id', 'url', 'album', 'quantity', 'date_added']


class ShoppingCartSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(read_only=True, view_name='customuser-detail')
    items = ShoppingCartItemSerializer(many=True)

    class Meta:
        model = ShoppingCart
        fields = ['url', 'owner', 'items']


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(many=True)
    shopping_cart = ShoppingCartSerializer()

    class Meta:
        model = CustomUser
        fields = ['id', 'url', 'username', 'reviews', 'shopping_cart']
