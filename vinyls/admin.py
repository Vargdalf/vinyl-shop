from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from vinyls.models import User, Genre, Album, Track, Review

admin.site.register(User, UserAdmin)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Review)
