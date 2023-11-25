from rest_framework import serializers
from .models import RangPlayer, Teams, DotaHeroes, PlayerDota2, GameDota2, TeamDota2, PlayerGameStats

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'

class RangPlayerSerializer(serializers.ModelSerializer):
    teams = serializers.StringRelatedField()
    class Meta:
        model = RangPlayer
        fields = '__all__'

class DotaHeroesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DotaHeroes
        fields = '__all__'

class TeamDota2Serializer(serializers.ModelSerializer):
    class Meta:
        model = TeamDota2
        fields = '__all__'

class PlayerDota2Serializer(serializers.ModelSerializer):
    team = TeamDota2Serializer()
    class Meta:
        model = PlayerDota2
        fields = '__all__'

class GameDota2Serializer(serializers.ModelSerializer):
    class Meta:
        model = GameDota2
        fields = '__all__'



class PlayerGameStatsSerializer(serializers.ModelSerializer):
    game = GameDota2Serializer()
    hero = DotaHeroesSerializer()
    player = PlayerDota2Serializer()
    class Meta:
        model = PlayerGameStats
        fields = '__all__'







