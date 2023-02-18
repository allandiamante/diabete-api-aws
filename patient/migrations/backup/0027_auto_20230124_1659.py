# Generated by Django 2.2.5 on 2023-01-24 19:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0026_hrvnonlinear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='alpha1',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='alpha2',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='area_sodp_rr',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='area_sodp_rr_log',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='csi',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ctm_r1',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ctm_r2',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ctm_r3',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='cvi',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='d2_10',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='d2_20',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ellipse_area',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_amostra_1',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_amostra_2',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_aprox_1_01',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_aprox_1_015',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_aprox_1_02',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_aprox_1_025',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_aprox_2_01',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_aprox_2_015',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_aprox_2_02',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_aprox_2_025',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_conditional',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_corrected_cond',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_fuzzy',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_multiescala_e3',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_multiescala_e5',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_permutation_1',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_permutation_2',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_shannon_1',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_shannon_2',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='ent_spectral',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='mean_dr1',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='mean_dr2',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='mean_dr3',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='mean_dr4',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='mean_dr5',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='norm_entropy',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='sd1',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='sd1_sd2_ratio',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrvnonlinear',
            name='sd2',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='bmi',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(450.0)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='bsa',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(150.0)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='weight',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(400.0)]),
        ),
    ]