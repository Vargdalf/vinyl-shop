from django.contrib.auth.models import User
from rest_framework import generics, permissions
from vinyls import models, serializers
from vinyls.permissions import IsOwnerOrReadOnly


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


class ReviewListView(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class ShoppingCartView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = models.ShoppingCart.objects.all()
    serializer_class = serializers.ShoppingCartSerializer


class ShoppingCartItemListView(generics.ListAPIView):
    queryset = models.ShoppingCartItem.objects.all()
    serializer_class = serializers.ShoppingCartSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
