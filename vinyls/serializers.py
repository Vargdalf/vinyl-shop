from rest_framework import serializers
from vinyls import models
from vinyls.models import Review, ShoppingCartItem


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True, many=True)
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    reviews = serializers.PrimaryKeyRelatedField(many=True, queryset=Review.objects.all())
    shopping_cart_items = serializers.PrimaryKeyRelatedField(many=True, queryset=ShoppingCartItem.objects.all())

    class Meta:
        model = models.Album
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Track
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'


class ShoppingCartSerializer(serializers.ModelSerializer):
    cart_items = serializers.PrimaryKeyRelatedField(many=True, queryset=ShoppingCartItem.objects.all())

    class Meta:
        model = models.ShoppingCart
        fields = '__all__'


class ShoppingCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ShoppingCartItem
        fields = '__all__'
