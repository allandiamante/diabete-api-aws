# Generated by Django 2.2.5 on 2023-01-20 18:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0024_collectdata_file_hrv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='can_status',
            field=models.PositiveSmallIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dbp_change',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dbp_empe',
            field=models.PositiveSmallIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dbp_repous',
            field=models.PositiveSmallIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mean_hr',
            field=models.PositiveSmallIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='obrienc_cs',
            field=models.PositiveSmallIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='rr_db',
            field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='rr_resting',
            field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='rr_standing',
            field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='rr_valsalva',
            field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sbp_change',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sbp_empe',
            field=models.PositiveSmallIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sbp_repous',
            field=models.PositiveSmallIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='state',
            field=models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2),
        ),
    ]
