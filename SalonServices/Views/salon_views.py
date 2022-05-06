from app.Services.error_handler import unhandled_error
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from SalonServices.Services import salon_services

User = get_user_model()

class SalonView(APIView):
    '''
        returs salons
        optional:
            latitude: int 
            longitude: int
            radius: int
        
        to shrink amount of response 
        for authorized user
    '''

    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):

        try:
            latitude = kwargs["latitude"] if "latitude" in kwargs else -1
            longitude = kwargs["longitude"] if "longitude" in kwargs else -1
            radius = kwargs["radius"] if "radius" in kwargs else -1

            response_value = salon_services.get_salons(latitude, longitude, radius)

        except Exception as e:
            print(e)
            return unhandled_error()

        return Response(response_value, status=200)
