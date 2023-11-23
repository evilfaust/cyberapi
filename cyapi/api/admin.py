from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import RangPlayer, Teams

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
