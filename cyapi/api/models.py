from django.db import models

# Create your models here.
class Teams(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'



class RangPlayer(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    teams = models.ForeignKey(Teams, on_delete=models.CASCADE)
    kills = models.FloatField(blank=True, default=0)
    dead = models.FloatField(blank=True, default=0)
    kd = models.FloatField(blank=True, default=0)

    def __str__(self):
        return f'{self.name} [{self.teams}] {self.kills}'


