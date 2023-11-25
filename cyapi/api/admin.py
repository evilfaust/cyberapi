from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import RangPlayer, Teams, TeamDota2, PlayerDota2, GameDota2, DotaHeroes, PlayerGameStats

class RangPlayerResource(resources.ModelResource):
    class Meta:
        model = RangPlayer

class RangPlayerAdmin(ImportExportModelAdmin):
    resource_classes = [RangPlayerResource]


class TeamsResource(resources.ModelResource):
    class Meta:
        model = Teams

class TeamsAdmin(ImportExportModelAdmin):
    resource_classes = [TeamsResource]

admin.site.register(Teams, TeamsAdmin)
admin.site.register(RangPlayer, RangPlayerAdmin)

class DotaHeroesResource(resources.ModelResource):
    class Meta:
        model = DotaHeroes

class DotaHeroesAdmin(ImportExportModelAdmin):
    resource_classes = [DotaHeroesResource]

class PlayerDota2Resource(resources.ModelResource):
    class Meta:
        model = PlayerDota2

class PlayerDota2Admin(ImportExportModelAdmin):
    resource_classes = [PlayerDota2Resource]

class TeamDota2Resource(resources.ModelResource):
    class Meta:
        model = TeamDota2

class PlayerDota2Admin(ImportExportModelAdmin):
    resource_classes = [TeamDota2Resource]

admin.site.register(TeamDota2, PlayerDota2Admin)
admin.site.register(PlayerDota2, PlayerDota2Admin)
admin.site.register(GameDota2)
admin.site.register(DotaHeroes, DotaHeroesAdmin)

admin.site.register(PlayerGameStats)