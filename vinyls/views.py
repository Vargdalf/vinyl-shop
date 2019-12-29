from rest_framework import generics
from vinyls import models, serializers


class GenreListView(generics.ListAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class AlbumListView(generics.ListAPIView):
    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer


class AlbumDetailView(generics.RetrieveAPIView):
    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer


class TrackListView(generics.ListAPIView):
    queryset = models.Track.objects.all()
    serializer_class = serializers.TrackSerializer


class ReviewListView(generics.ListAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class ReviewDetailView(generics.RetrieveAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class ShoppingCartView(generics.RetrieveAPIView):
    queryset = models.ShoppingCart.objects.all()
    serializer_class = serializers.ShoppingCartSerializer


class ShoppingCartItemListView(generics.ListAPIView):
    queryset = models.ShoppingCartItem.objects.all()
    serializer_class = serializers.ShoppingCartSerializer
