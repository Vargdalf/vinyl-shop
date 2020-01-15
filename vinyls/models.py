from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify


class CustomUser(AbstractUser):
    slug = models.SlugField(null=False, unique=True, default='')

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super(CustomUser, self).save(*args, **kwargs)

    @classmethod
    def post_create(cls, sender, instance, created, *args, **kwargs):
        if not created:
            return
        ShoppingCart.objects.create(owner=instance)
        WishList.objects.create(owner=instance)


post_save.connect(CustomUser.post_create, sender=CustomUser)


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=False, unique=True, default='')
    artist = models.CharField(max_length=150)
    year = models.DateField()
    genres = models.ManyToManyField(Genre, related_name='albums')
    duration = models.TimeField()
    label = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        ordering = ['artist']

    def __str__(self):
        return f'{self.title} by {self.artist}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify([self.artist, self.title])
        return super(Album, self).save(*args, **kwargs)


class Track(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField()
    duration = models.TimeField()
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order}: {self.title}'


class Review(models.Model):
    owner = models.ForeignKey(CustomUser, related_name='reviews', on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.TextField()
    slug = models.SlugField(null=False, unique=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.rating}/5 - {self.owner}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify([self.owner.username, self.album.title])
        return super(Review, self).save(*args, **kwargs)


class ShoppingCart(models.Model):
    owner = models.OneToOneField(CustomUser, related_name='shopping_cart', on_delete=models.CASCADE, primary_key=True)
    slug = models.SlugField(null=False, unique=True, default='')

    class Meta:
        ordering = ['owner']

    def __str__(self):
        return f'{self.owner}\'s Cart'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify([self.owner.username, 'cart'])
        return super(ShoppingCart, self).save(*args, **kwargs)

    def clear_cart(self):
        self.items.all().delete()

    def add_album(self, album, quantity=1):
        items = self.items.filter(album=album)
        if len(items) == 0:
            self.items.create(album=album)
        else:
            item = items[0]
            item.quantity += quantity
            item.save()

    def is_empty(self):
        return self.num_items() == 0

    def num_items(self):
        total = 0
        for item in self.all_items():
            total += item.quantity
        return total

    def all_items(self):
        return self.items.all()

    def get_total(self):
        total = 0
        for item in self.all_items():
            total += item.album.price * item.quantity
        return int(total)


class ShoppingCartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, related_name='items', on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name='shopping_cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'{self.album} x {self.quantity}'


class WishList(models.Model):
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    slug = models.SlugField(null=False, unique=True, default='')

    class Meta:
        ordering = ['owner']

    def __str__(self):
        return f'{self.owner}\'s Wishlist'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify([self.owner.username, 'wishlist'])
        return super(WishList, self).save(*args, **kwargs)

    def clear_wishlist(self):
        self.items.all().delete()

    def add_album(self, album):
        items = self.items.filter(album=album)
        if len(items) == 0:
            self.items.create(album=album)
        else:
            item = items[0]
            item.quantity += 1
            item.save()

    def all_items(self):
        return self.items.all()


class WishListItem(models.Model):
    wishlist = models.ForeignKey(WishList, related_name='items', on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name='wishlist_items', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'{self.album.title} on {self.wishlist.owner}\'s Wishlist'
