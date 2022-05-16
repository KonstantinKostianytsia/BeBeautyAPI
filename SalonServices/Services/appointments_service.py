from SalonServices.serializers import AppointmentsSerializer
from SalonServices.models import Appointments
from SalonServices.Services.services_service import get_service_by_id
from SalonServices.Services.employee_service import get_employee_by_id
from SalonServices.Services.salon_services import get_salon_by_id


def get_appointment_by_id(id: int):
    appointment_query_set = Appointments.objects.get(id=id)
    appointment = AppointmentsSerializer(appointment_query_set, many=False).data

    services_ids = appointment["services_ids"].split(", ")
    services = []
    for service_id in services_ids:
        services.append(get_service_by_id(int(service_id)))
    
    employee_id = int(appointment["employee_id"])
    employee = get_employee_by_id(employee_id)

    salon_id = int(employee["salon_id"])
    salon = get_salon_by_id(salon_id)


    return {
        "id": appointment["id"],
        "employee": {
            "id": employee["id"],
            "first_name": employee["first_name"],
            "last_name": employee["last_name"],
            "amount_of_votes": employee["amount_of_votes"],
            "sum_of_stars": employee["sum_of_stars"],
            "is_manager": employee["is_manager"],
            "salon": salon,
            "is_even_days": employee["is_even_days"],
            "phone_number": employee["phone_number"],
        },
        "user_id": appointment["user_id"],
        "end_date": appointment["end_date"],
        "services": services,
        "start_date": appointment["start_date"],
    }