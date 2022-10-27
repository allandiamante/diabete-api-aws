# Generated by Django 3.1.2 on 2022-10-27 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('temperatuer', models.DecimalField(decimal_places=2, max_digits=12)),
                ('description', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
            ],
        ),
    ]
