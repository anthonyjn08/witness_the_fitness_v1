from django.contrib import admin
from .models import Sports


@admin.register(Sports)
class SportsAdmin(admin.ModelAdmin):

    list_display = ('sport_category', 'sport_type', 'trainer_id', 'sport_cost', 'sport_description')
    search_fields = ['sport_category', 'sport_type']
