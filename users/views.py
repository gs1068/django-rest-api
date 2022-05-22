from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters

from .models import User
from .serializer import UserSerializer
from rest_framework.decorators import api_view
# Create your views here.

# ViewSetはCRUDを実装を肩代わりしてくれる
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
