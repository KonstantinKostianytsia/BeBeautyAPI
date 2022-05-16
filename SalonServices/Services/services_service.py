from SalonServices.models import *
from SalonServices.serializers import *

def get_service_by_id(service_id: int):
    service = Service.objects.get(id=service_id)
    serialized_service = ServiceSerializer(service, many=False).data
    return serialized_service