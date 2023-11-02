from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from . import serializers
from .models import RangPlayer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class RangPlayerList(generics.ListCreateAPIView):
    queryset =RangPlayer.objects.all()
    serializer_class = serializers.RangPlayerSerializer
