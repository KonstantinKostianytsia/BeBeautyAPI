# Generated by Django 4.0.4 on 2022-05-14 19:52

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('SalonServices', '0011_remove_appointments_service_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
