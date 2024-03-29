# Generated by Django 2.2.5 on 2023-01-26 19:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0045_auto_20230126_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='physical_activity',
            field=models.PositiveSmallIntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Physical Activity'),
        ),
    ]
