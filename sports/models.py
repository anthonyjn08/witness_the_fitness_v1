from django.db import models
from trainers.models import Trainers


class Sports(models.Model):
    trainer_id = models.ForeignKey(Trainers, on_delete=models.CASCADE)
    sport_type = models.CharField(max_length=100, null=False, blank=False)
    sport_category = models.CharField(max_length=100, null=False, blank=False)
    sport_description = models.TextField(blank=True)
    sport_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                     null=False, blank=False)
    sport_location = models.CharField(max_length=100, null=False, blank=False)
    sport_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.sport_type

    class Meta:
        verbose_name_plural = 'Sports'
