# Generated by Django 3.2 on 2022-10-02 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0005_alter_trainers_trainer_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainers',
            name='trainer_category',
            field=models.CharField(max_length=20, null=True),
        ),
    ]