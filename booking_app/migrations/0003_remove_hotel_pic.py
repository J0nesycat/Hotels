# Generated by Django 4.2.13 on 2024-05-24 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0002_hotel_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='pic',
        ),
    ]