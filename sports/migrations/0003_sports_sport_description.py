# Generated by Django 3.2 on 2022-10-07 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_rename_sport_sports_sport_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='sports',
            name='sport_description',
            field=models.TextField(blank=True),
        ),
    ]
