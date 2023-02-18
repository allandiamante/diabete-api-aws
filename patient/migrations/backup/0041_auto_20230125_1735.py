# Generated by Django 2.2.5 on 2023-01-25 20:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0040_auto_20230125_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collectdata',
            name='file_hrv',
        ),
        migrations.AddField(
            model_name='collectdata',
            name='ecg_signal',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Observations'),
        ),
        migrations.AlterField(
            model_name='collectdata',
            name='abp',
            field=models.BooleanField(default=False, null=True, verbose_name='Abp'),
        ),
        migrations.AlterField(
            model_name='collectdata',
            name='abspathrecord_times',
            field=models.PositiveSmallIntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Abspathrecord Times'),
        ),
        migrations.AlterField(
            model_name='collectdata',
            name='collected_data',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Collected Data'),
        ),
        migrations.AlterField(
            model_name='collectdata',
            name='device',
            field=models.PositiveSmallIntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Device'),
        ),
        migrations.AlterField(
            model_name='collectdata',
            name='ecg',
            field=models.BooleanField(default=False, null=True, verbose_name='Ecg'),
        ),
        migrations.AlterField(
            model_name='collectdata',
            name='emg',
            field=models.BooleanField(default=False, null=True, verbose_name='Emg'),
        ),
        migrations.AlterField(
            model_name='collectdata',
            name='observations',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Ecg Signal'),
        ),
        migrations.AlterField(
            model_name='collectdata',
            name='patient_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.Patient', verbose_name='Patient Data'),
        ),
        migrations.AlterField(
            model_name='collectdata',
            name='ppg',
            field=models.BooleanField(default=False, null=True, verbose_name='Ppg'),
        ),
        migrations.AlterField(
            model_name='collectdata',
            name='sampling_freq_hz',
            field=models.PositiveSmallIntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Sampling Freq_Hz'),
        ),
        migrations.AlterField(
            model_name='collectdata',
            name='study',
            field=models.PositiveSmallIntegerField(choices=[(1, 'DOC_SC'), (2, 'Extra_data_Prof_jan22')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Study'),
        ),
    ]