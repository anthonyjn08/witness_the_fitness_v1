from django.db import models


class Trainers(models.Model):
    trainer_name = models.CharField(max_length=100, null=False, blank=False)
    trainer_email = models.EmailField(max_length=254, null=False, blank=False)
    trainer_phone_number = models.CharField(max_length=20, null=False, blank=False)
    trainer_bio = models.TextField(null=False)
    trainer_image = models.ImageField(default="trainer_placholder")

    def __str__(self):
        return self.trainer_name
