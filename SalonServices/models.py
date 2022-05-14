from django.db import models
import datetime

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    amount_of_votes = models.IntegerField(default=0)
    sum_of_stars = models.IntegerField(default=0)
    is_manager = models.BooleanField(default=False)
    salon_id = models.IntegerField(default=0)
    is_even_days = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Salon(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.FloatField(default=50)
    longitude = models.FloatField(default=120)
    name = models.CharField(max_length=120, default='BeBeauty')
    address = models.CharField(max_length=120, default='Kharkiv')
    manager_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=200, default='')
    duration_of_service = models.IntegerField(default=120)

    def __str__(self):
        return self.service_name

class Appointments(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.IntegerField(default=0)
    services_ids = models.CharField(max_length=50,default="") #joined services ids with comma
    user_id = models.IntegerField(default=0)
    start_date = models.DateTimeField('Start Date', default=datetime.datetime.today)
    end_date = models.DateTimeField('End Date', default=datetime.datetime.today)

    def __str__(self):
        return str(self.user_id + " " + self.services_ids)

class Skill(models.Model):
    employee_id = models.IntegerField(default=0)
    service_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.employee_id)


