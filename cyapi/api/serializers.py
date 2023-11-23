from rest_framework import serializers
from .models import RangPlayer, Teams

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'

class RangPlayerSerializer(serializers.ModelSerializer):
    teams = serializers.StringRelatedField()
    class Meta:
        model = RangPlayer
        fields = '__all__'
