from django.urls import path, include
from vinyls import views

urlpatterns = [
    path('', views.AlbumListView.as_view(), name='root'),
    path('api-auth/', include('rest_framework.urls')),
    path('genres/', views.GenreListView.as_view(), name='genres_list'),
    path('albums/', views.AlbumListView.as_view(), name='albums_list'),
    path('albums/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('tracks/', views.TrackListView.as_view(), name='tracks_list'),
    path('reviews/', views.ReviewListView.as_view(), name='reviews_list'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review_detail'),
    path('shopping-cart/<int:pk>', views.ShoppingCartView.as_view(), name='shopping_cart'),
    path('shopping-cart-items/', views.ShoppingCartItemListView.as_view(), name='shopping_cart_items_list'),
    path('users/', views.UserList.as_view(), name='users_list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
]
