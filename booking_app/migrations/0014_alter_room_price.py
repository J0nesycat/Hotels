# Generated by Django 4.2.13 on 2024-05-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0013_hotel_rooms_room_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]