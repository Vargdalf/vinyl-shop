from django.contrib.auth.models import User
from rest_framework import generics, permissions
from vinyls import models, serializers
from vinyls.permissions import IsOwnerOrReadOnly

# TODO: views
