# Generated by Django 2.2.5 on 2023-01-25 20:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0033_auto_20230124_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='physical_activity',
            field=models.PositiveSmallIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]