# Generated by Django 2.2.5 on 2023-01-24 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0031_auto_20230124_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectdata',
            name='observations',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
