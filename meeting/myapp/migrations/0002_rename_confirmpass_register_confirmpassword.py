# Generated by Django 5.0.2 on 2024-02-25 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='Confirmpass',
            new_name='Confirmpassword',
        ),
    ]