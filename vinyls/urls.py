from django.urls import path, include
from rest_framework.routers import DefaultRouter

from vinyls.views import GenreListView, AlbumViewSet, ReviewViewSet, UserViewSet, ShoppingCartViewSet, \
    ShoppingCartItemViewSet, GoogleLoginView

router = DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'users', UserViewSet)
router.register(r'cart', ShoppingCartViewSet)
router.register(r'cart-item', ShoppingCartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/google/', GoogleLoginView.as_view(), name='google_login'),
    path('genres/', GenreListView.as_view(), name='genre-list'),
]
