from rest_framework import generics, permissions, viewsets
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

from vinyls.models import Genre, Album, Review, CustomUser, ShoppingCart
from vinyls.permissions import IsOwnerOrReadOnly, IsOwner
from vinyls.serializers import GenreSerializer, AlbumSerializer, ReviewSerializer, CustomUserSerializer, \
    ShoppingCartSerializer


class GenreListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class ShoppingCartEditView(generics.RetrieveUpdateAPIView):
    serializer_class = ShoppingCartSerializer
    permission_classes = [IsOwner]
    lookup_field = 'slug'

    def get_queryset(self):
        return ShoppingCart.objects.all()


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
