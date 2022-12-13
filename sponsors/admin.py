from django.contrib import admin
from .models import Sponsors


@admin.register(Sponsors)
class SponsorsAdmin(admin.ModelAdmin):

    list_display = ('sponsor_name', 'sponsor_bio')
    search_fields = ['sponsor_name']
