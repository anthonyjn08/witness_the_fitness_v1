from django.contrib import admin
from .models import Classes


@admin.register(Sports)
class SportsAdmin(admin.ModelAdmin):

    list_display = ('sport_category', 'sport', 'trainer_id', 'sport_cost')
    search_fields = ['sport_category', 'sport']
