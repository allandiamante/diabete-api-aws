# Generated by Django 2.2.5 on 2023-01-20 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0023_auto_20230120_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectdata',
            name='file_hrv',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
