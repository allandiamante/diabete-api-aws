# Generated by Django 2.2.5 on 2023-02-03 17:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0052_auto_20230203_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examsresult',
            name='hb_g_dl',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Hb (g_dL)'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='type_dm',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Tipo 1'), (2, 'Tipo 2'), (3, 'Tipo 3 Gestacional')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)], verbose_name='Type DM'),
        ),
    ]
