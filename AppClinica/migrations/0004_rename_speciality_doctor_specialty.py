# Generated by Django 4.2.6 on 2023-11-10 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppClinica', '0003_rename_type_doctor_mode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='speciality',
            new_name='specialty',
        ),
    ]
