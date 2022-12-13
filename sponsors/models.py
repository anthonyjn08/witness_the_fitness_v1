from django.db import models


class Sponsors(models.Model):
    sponsor_name = models.CharField(max_length=100, null=False, blank=False)
    sponsor_bio = models.TextField(null=False)
    sponsor_image = models.ImageField(null=True, blank=True)
    sponsor_website = models.TextField(null=False)

    def __str__(self):
        return self.sponsor_name

    class Meta:
        db_table = 'Sponsors'
        # Add verbose name
        verbose_name = 'Sponsor'
