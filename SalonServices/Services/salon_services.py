from SalonServices.Utills.salon_utils import structorize_salon
from SalonServices.models import Salon
from SalonServices.serializers import *
from SalonServices.Services.employee_service import get_employee_by_id
from SalonServices.Services.services_service import get_service_by_id

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

def get_salon_by_id(salon_id: int):
    salon_query_set = Salon.objects.get(id=salon_id)
    salon = SalonSerializer(salon_query_set).data
    manager = get_employee_by_id(salon['manager_id'])

    return structorize_salon(salon, manager)

def create_appointment(user_id, data):
    try:
        employee_id = int(data['employee_id'])
        start_date = datetime.datetime.strptime(data['start_date'], '%Y-%m-%dT%H:%M:%S.000Z')
        end_date = datetime.datetime.strptime(data['end_date'], '%Y-%m-%dT%H:%M:%S.000Z')
        services_ids = data['services_ids']

        Appointments.objects.create(employee_id=employee_id, user_id=user_id,
                                    start_date=start_date, end_date=end_date, 
                                    services_ids=services_ids)
        return "Appointment were booked"
    except Exception as e:
        print(e)
        raise(e)


def get_user_appointments(user_id):
    appointments = Appointments.objects.filter(user_id=user_id)
    serialized_appointments = AppointmentsSerializer(appointments, many=True).data
    response = []
    for appointment in serialized_appointments:
        services_ids = appointment["services_ids"].split(", ")
        services = []
        for service_id in services_ids:
            services.append(get_service_by_id(int(service_id)))
        
        response.append({
            "id": appointment["id"],
            "employee_id": appointment["employee_id"],
            "start_date": appointment["start_date"],
            "end_date": appointment["end_date"],
            "services": services
        })
        
    return response