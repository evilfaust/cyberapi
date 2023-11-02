from rest_framework import serializers
from .models import RangPlayer

class RangPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RangPlayer
        fields = '__all__'