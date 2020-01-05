from django.urls import path, include
from vinyls import views

urlpatterns = [
    path('genres/', views.GenreListView.as_view()),
    path('albums/', views.AlbumListView.as_view()),
    path('albums/<int:pk>/', views.AlbumDetailView.as_view()),
    path('reviews/', views.ReviewListView.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view()),
    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view()),
]

# Login
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
