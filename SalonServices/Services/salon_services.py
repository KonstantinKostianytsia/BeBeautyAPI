from SalonServices.Utills.salon_utils import structorize_salon
from tkinter import E
from SalonServices.models import Salon
from SalonServices.serializers import *

def get_salons(latitude: float, longitude: float, radius: int):
    try:
        salons = Salon.objects.all()
        response = []
        serialized_salons = SalonSerializer(salons, many=True).data
        for salon in serialized_salons:
            manager = get_employee_by_id(salon['manager_id'])
            response.append(structorize_salon(salon, manager))
    except Exception as e:
        print(e)
        raise e
    
    return response

def get_employee_by_id(employee_id: int):
    try:
        employee = Employee.objects.get(id = employee_id)
        serialized_employee = EmployeeSerializer(employee, many=False).data
        print(serialized_employee)
    except Exception as e:
        print(e)
        raise e
    
    return serialized_employee
