# Generated by Django 4.2.6 on 2023-11-08 07:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppClinica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='idioms',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=120), size=None),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='type',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=120), size=None),
        ),
    ]