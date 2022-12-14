from django.db import models


class Trainers(models.Model):
    trainer_name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    trainer_email = models.EmailField(max_length=254, null=False, blank=False)
    trainer_phone_number = models.CharField(max_length=20, null=False,
                                            blank=False)
    trainer_bio = models.TextField(null=False)
    trainer_image = models.ImageField(null=True, blank=True)
    trainer_category = models.CharField(max_length=20, blank=False, null=True)

    def __str__(self):
        return self.trainer_name

    class Meta:
        db_table = 'Trainers'
        # Add verbose name
        verbose_name = 'Trainer'
