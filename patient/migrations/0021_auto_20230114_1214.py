# Generated by Django 2.2.5 on 2023-01-14 15:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0020_auto_20230113_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='height',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)]),
        ),
    ]
