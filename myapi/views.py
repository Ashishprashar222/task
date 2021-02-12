from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from myapi.serializers import userSerializer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all().order_by('-date_joined')
    serializer_class=userSerializer
    permission_classes=[permissions.IsAuthenticated]