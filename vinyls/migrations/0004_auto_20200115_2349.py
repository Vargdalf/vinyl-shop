# Generated by Django 3.0.1 on 2020-01-15 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinyls', '0003_customuser_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
