# Generated by Django 4.2.13 on 2024-05-30 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0022_alter_room_number_of_guests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='number_of_rooms',
        ),
    ]
