from django.contrib import admin
from .models import Buildings


# Register your models here.
class BuildingsAdmin(admin.ModelAdmin):
    """
    Buildings
    """
    list_display = ('id', 'building_id', 'name', 'households', 'location', 'image', 'created', 'updated')


admin.site.register(Buildings, BuildingsAdmin)
