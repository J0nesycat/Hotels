# Generated by Django 4.2.13 on 2024-05-30 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0021_alter_room_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='number_of_guests',
            field=models.IntegerField(),
        ),
    ]