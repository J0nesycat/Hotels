# Generated by Django 4.2.13 on 2024-05-24 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0005_remove_hotel_rooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='rooms',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking_app.room'),
        ),
    ]