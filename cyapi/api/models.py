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

class DotaHeroes(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    role = models.CharField(max_length=100, blank=True, default='')
    attacktype = models.CharField(max_length=100, blank=True, default='')
    tooltipe = models.CharField(max_length=100, blank=True, default='')
    images = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=100, blank=True, default='')
    def __str__(self):
        return f'{self.title} {self.type}'

class TeamDota2(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class PlayerDota2(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    team = models.ForeignKey(TeamDota2, on_delete=models.CASCADE)
    steamid = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return f'{self.name} [{self.team}]'


class GameDota2(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    date = models.DateField(auto_now=False)

    def __str__(self):
        return f'{self.title}  {self.date}'

class PlayerGameStats(models.Model):
    game = models.ForeignKey(GameDota2, on_delete=models.CASCADE)
    player = models.ForeignKey(PlayerDota2, on_delete=models.CASCADE)
    hero = models.ForeignKey(DotaHeroes, on_delete=models.CASCADE, default=1)
    gold = models.IntegerField()
    kills = models.IntegerField()
    dead = models.IntegerField()
    assists = models.IntegerField()

    def __str__(self):
        return f'{self.player} stats for Game {self.game}'

