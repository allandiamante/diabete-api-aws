# Generated by Django 3.1.2 on 2022-10-27 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_auto_20221027_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conditions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drge', models.BooleanField(default=False)),
                ('vitiligo', models.BooleanField(default=False)),
                ('doenca_celiaca', models.BooleanField(default=False)),
                ('doenca_pulmonar', models.BooleanField(default=False)),
                ('ace_arb', models.BooleanField(default=False)),
                ('tireoide', models.BooleanField(default=False)),
                ('retinopathy', models.BooleanField(default=False)),
                ('nephropathy', models.BooleanField(default=False)),
                ('peripheral_neuropathy', models.BooleanField(default=False)),
                ('pn_symptoms', models.CharField(max_length=200)),
                ('pn_signs', models.CharField(max_length=200)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
