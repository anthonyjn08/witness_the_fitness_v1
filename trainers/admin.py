from django.contrib import admin
from .models import Trainers


@admin.register(Trainers)
class TrainersAdmin(admin.ModelAdmin):
    list_display = (
        'trainer_name',
        'trainer_email',
    )