# Generated by Django 3.1.2 on 2022-12-14 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0016_auto_20221213_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='hrvfreq',
            name='file_hrvfreq',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='hrvtime',
            name='file_hrvtime',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
