from django.urls import path, include
from rest_framework.routers import DefaultRouter

from vinyls.views import GenreListView, AlbumViewSet, ReviewViewSet, UserViewSet

router = DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('genres/', GenreListView.as_view(), name='genre-list'),
]
