from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from . import serializers
from .models import RangPlayer, GameDota2, PlayerGameStats
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class RangPlayerList(generics.ListCreateAPIView):
    queryset = RangPlayer.objects.all()
    serializer_class = serializers.RangPlayerSerializer


class GameDota2List(generics.ListCreateAPIView):
    queryset = PlayerGameStats.objects.all()
    serializer_class = serializers.PlayerGameStatsSerializer

class GameDota2GameList(generics.ListAPIView):
    serializer_class = serializers.PlayerGameStatsSerializer

    def get_queryset(self):
        game_id = self.kwargs['game_id']  # Получаем идентификатор игры из URL
        queryset = PlayerGameStats.objects.filter(game_id=game_id)
        return queryset