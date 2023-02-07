# Generated by Django 2.2.5 on 2023-02-01 20:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0047_auto_20230126_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectdata',
            name='abp',
            field=models.BooleanField(default=False, null=True, verbose_name='ABP'),
        ),
        migrations.AlterField(
            model_name='collectdata',
            name='ecg',
            field=models.BooleanField(default=False, null=True, verbose_name='ECG'),
        ),
        migrations.AlterField(
            model_name='collectdata',
            name='emg',
            field=models.BooleanField(default=False, null=True, verbose_name='EMG'),
        ),
        migrations.AlterField(
            model_name='collectdata',
            name='ppg',
            field=models.BooleanField(default=False, null=True, verbose_name='PPG'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='height',
            field=models.FloatField(help_text='1.82', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)], verbose_name='Height (m)'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='weight',
            field=models.FloatField(help_text='60.5', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(400.0)], verbose_name='Weight (kg)'),
        ),
    ]
