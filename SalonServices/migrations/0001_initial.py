# Generated by Django 4.0.4 on 2022-05-04 18:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_id', models.IntegerField(default=0)),
                ('service_id', models.IntegerField(default=0)),
                ('user_id', models.IntegerField(default=0)),
                ('start_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('end_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('amount_of_votes', models.IntegerField(default=0)),
                ('sum_of_stars', models.IntegerField(default=0)),
                ('is_manager', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('latitude', models.IntegerField(default=50)),
                ('longitude', models.IntegerField(default=120)),
                ('name', models.CharField(default='BeBeauty', max_length=120)),
                ('address', models.CharField(default='Kharkiv', max_length=120)),
                ('manager_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=200)),
                ('duration_of_service', models.IntegerField(default=120)),
            ],
        ),
    ]
