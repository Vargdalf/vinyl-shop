from django.contrib.auth.models import User
from rest_framework import serializers
from vinyls import models
from vinyls.models import Review, ShoppingCartItem, ShoppingCart


class UserSerializer(serializers.ModelSerializer):
    reviews = serializers.PrimaryKeyRelatedField(many=True, queryset=Review.objects.all())
    cart = serializers.PrimaryKeyRelatedField(many=True, queryset=ShoppingCart.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'reviews', 'cart']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    reviews = serializers.PrimaryKeyRelatedField(many=True, queryset=Review.objects.all())

    class Meta:
        model = models.Album
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Track
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = models.Review
        fields = '__all__'


class ShoppingCartSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.username')
    cart_items = serializers.PrimaryKeyRelatedField(many=True, queryset=ShoppingCartItem.objects.all())

    class Meta:
        model = models.ShoppingCart
        fields = '__all__'


class ShoppingCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ShoppingCartItem
        fields = '__all__'
