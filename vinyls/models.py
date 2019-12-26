from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


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


class Track(models.Model):
    title = models.CharField(max_length=100)
    duration = models.TimeField()
    album = models.ForeignKey(Album, on_delete=CASCADE)

    def __str__(self):
        return f'{self.album.title} - \'{self.title}\''


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE)
    album = models.ForeignKey(Album, on_delete=CASCADE)
    rating = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating}/5 - {self.author}'


class ShoppingCart(models.Model):
    customer = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return f'{self.customer}\'s Cart'


class ShoppingCartItem(models.Model):
    album = models.ForeignKey(Album, on_delete=CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(ShoppingCart, on_delete=CASCADE)

    def __str__(self):
        return f'{self.cart.customer} - {self.album}'
