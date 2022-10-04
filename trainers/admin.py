from django.contrib import admin
from .models import Trainers


@admin.register(Trainers)
class TrainersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'trainer_name',
        'trainer_email',
    )
    prepopulated_fields = {'slug': ('trainer_name',)}
