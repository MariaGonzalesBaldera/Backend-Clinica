# Generated by Django 4.2.6 on 2023-11-10 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppClinica', '0004_rename_speciality_doctor_specialty'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Specialties',
            new_name='Specialty',
        ),
    ]