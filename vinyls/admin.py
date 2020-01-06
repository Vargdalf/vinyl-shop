from django.contrib import admin
from vinyls.models import Genre, Album, Track, Review, User

admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Review)
admin.site.register(User)
