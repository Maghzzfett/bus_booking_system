# Generated by Django 4.2 on 2023-06-06 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ussd_booking', '0009_trip_departure_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Trip',
            new_name='Schedule',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='trip',
            new_name='schedule',
        ),
    ]