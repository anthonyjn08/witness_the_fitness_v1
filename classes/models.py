from django.db import models
from trainers.models import Trainers

class Classes(models.Model):
    trainer_id = models.ForeignKey(Trainers, on_delete=models.CASCADE)
    class_sport = models.CharField(max_length=100, null=False, blank=False)
    class_category = models.CharField(max_length=100, null=False, blank=False)
    class_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    class_location = models.CharField(max_length=100, null=False, blank=False)
    class_image = models.ImageField(default='placeholder')

    def __str__(self):
        return self.class_sport
