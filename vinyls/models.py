from django.contrib.auth.models import User
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)
    year = models.DateField()
    genre = models.ManyToManyField(Genre)
    duration = models.TimeField()
    label = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.title} by {self.artist}'

    class Meta:
        ordering = ['artist']


class Track(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField()
    duration = models.TimeField()
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.order}: {self.title}'


class Review(models.Model):
    owner = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating}/5 - {self.owner}'


# TODO: clear_basket, add_product, get_total, is_empty, total_discount,
class ShoppingCart(models.Model):
    owner = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.owner}\'s Cart'


class ShoppingCartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, related_name='cart_items', on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name='shopping_cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cart.owner} - {self.album}'

    class Meta:
        ordering = ['date_added', 'pk']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wish_list = ''


# TODO: add_product
class WishList(models.Model):
    owner = models.ForeignKey(User, related_name='wishlist', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.owner}\'s Wishlist'


class WishListItem(models.Model):
    wishlist = models.ForeignKey(WishList, related_name='list_items', on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name='wishlist_items', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added', 'pk']

    def __str__(self):
        return f'{self.album.title} on {self.wishlist.owner}\'s Wishlist'
