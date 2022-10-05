from django.contrib import admin
from .models import Classes


@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):

    list_display = ('class_category', 'class_sport', 'trainer_id', 'class_cost')
    search_fields = ['class_category', 'class_sport']
    
