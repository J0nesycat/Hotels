# Generated by Django 4.2.13 on 2024-05-30 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0025_reservation_full_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]