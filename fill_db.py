import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')
django.setup()

from django.contrib.auth.models import User
from vinyls.models import Genre, Album, Track, Review, ShoppingCart, WishList


def add_objects():
    User.objects.create_user('user1', password='testpass')
    User.objects.create_user('user2', password='testpass')
    User.objects.create_user('user3', password='testpass')

    Genre.objects.create(name='Rock')
    Genre.objects.create(name='Jazz')
    Genre.objects.create(name='Metal')

    # TODO: more objects
