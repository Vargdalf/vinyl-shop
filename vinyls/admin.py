from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from vinyls.models import CustomUser, Genre, Album, Track, Review

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Review)
