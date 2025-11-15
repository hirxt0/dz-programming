from django.contrib import admin
from .models import Starship

@admin.register(Starship)
class StarshipAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'starship_class', 'manufacturer']
    search_fields = ['name', 'model']
    list_filter = ['starship_class']