from django.urls import path, include
from vinyls import views

urlpatterns = [
    path('', views.api_root),
    path('genres/', views.GenreListView.as_view(), name='genre-list'),
    path('albums/', views.AlbumListView.as_view(), name='album-list'),
    path('albums/<int:pk>/', views.AlbumDetailView.as_view(), name='album-detail'),
    path('reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
]

# Login
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
