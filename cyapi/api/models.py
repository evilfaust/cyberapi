from django.db import models

# Create your models here.
class RangPlayer(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    teams = models.CharField(max_length=100, blank=True, default='')
    kills = models.FloatField(blank=True, default=0)

    def __str__(self):
        return f'{self.name} {self.kills}'