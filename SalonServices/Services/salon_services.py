from SalonServices.Utills.salon_utils import structorize_salon
from SalonServices.models import Salon
from SalonServices.serializers import *
from SalonServices.Services.employee_service import get_employee_by_id

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
