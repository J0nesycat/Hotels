# Generated by Django 4.2.13 on 2024-06-01 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0029_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='confirmation_number',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
