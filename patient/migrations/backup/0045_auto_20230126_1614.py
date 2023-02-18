# Generated by Django 2.2.5 on 2023-01-26 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0044_auto_20230126_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrvtime',
            name='cv',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='hr_change',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='hti',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn20',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn50',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn_iqr',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn_kurt',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn_median',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn_mode',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn_skew',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='nn_variance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='pnn20_pr',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='pnn50_pr',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='rmssd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='sd_nn',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='sdsd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='si',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hrvtime',
            name='tinn',
            field=models.FloatField(blank=True, null=True),
        ),
    ]