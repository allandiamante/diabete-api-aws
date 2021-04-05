# Generated by Django 2.2.5 on 2020-03-31 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddOns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years_of_warranty', models.PositiveIntegerField(default=1)),
                ('insurence_plan', models.CharField(max_length=15)),
                ('finance_plan', models.CharField(default='unavailable', max_length=15)),
                ('car_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstApp.CarSpecs')),
            ],
        ),
    ]
