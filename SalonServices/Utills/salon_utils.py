from SalonServices.models import *


def structorize_salon(salon: Salon, employee: Employee):
    response = {}

    response['id'] = salon['id']
    response['latitude'] = salon['latitude']
    response['longitude'] = salon['longitude']
    response['name'] = salon['name']
    response['address'] = salon['address']
    response['manager'] = employee

    return response