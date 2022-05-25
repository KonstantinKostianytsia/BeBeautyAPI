from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'amount_of_votes', 'sum_of_stars', 'is_manager', 'salon_id', 'is_even_days', 'phone_number', 'avatar')
    
class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = ('id', 'latitude', 'longitude', 'name', 'address', 'manager_id')
    
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'service_name', 'description', 'duration_of_service')

class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ('id', 'employee_id', 'services_ids', 'user_id', 'start_date', 'end_date')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('employee_id', 'service_id')