# Generated by Django 4.2.13 on 2024-05-24 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0006_hotel_rooms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='rooms',
        ),
    ]