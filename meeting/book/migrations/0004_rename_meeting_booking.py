# Generated by Django 5.0.2 on 2024-03-24 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_rename_booking_meeting'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='meeting',
            new_name='Booking',
        ),
    ]
