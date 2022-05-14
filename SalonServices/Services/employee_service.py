from SalonServices.models import *
from SalonServices.serializers import *

def get_employee_by_id(employee_id: int):
    try:
        employee = Employee.objects.get(id = employee_id)
        serialized_employee = EmployeeSerializer(employee, many=False).data
    except Exception as e:
        print(e)
        raise e
    
    return serialized_employee

def get_employees_by_salon_id(salon_id: int):
    try:
        employees_query_set = Employee.objects.filter(salon_id = salon_id)
        employees = EmployeeSerializer(employees_query_set, many=True).data
    except Exception as e:
        print(e)
        raise(e)

    return employees

def get_employee_skills(employee_id: int):
    try:
        employee_skill_services = Skill.objects.filter(employee_id=employee_id)
        employee_skills_serialized = SkillSerializer(employee_skill_services, many=True).data
        response = []
        for service in employee_skills_serialized:
            service_query_set = Service.objects.get(id=service['service_id'])
            response.append(ServiceSerializer(service_query_set, many=False).data)
    except Exception as e:
        print(e)
        raise e    
    
    return response

def get_employee_appointments(employee_id: int, date: datetime):
    try:
        employee_appointments = Appointments.objects.filter(employee_id=employee_id, start_date__gte=date, start_date__lte=datetime.datetime(date.year, date.month, date.day,22,00,00))
        employee_appointments_serialized = AppointmentsSerializer(employee_appointments, many=True).data
    except Exception as e:
        print(e)
        raise e

    return employee_appointments_serialized

