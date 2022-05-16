from rest_framework.response import Response
from rest_framework.views import APIView
from app.Services.error_handler import handle_error, unhandled_error
from SalonServices.Services import appointments_service
from rest_framework.permissions import AllowAny, IsAuthenticated

class AppointmentView(APIView):

    permission_classes = (AllowAny, )

    def get(self, request):
        try:
            appointment_id = int(request.GET.get("id"))
            response = appointments_service.get_appointment_by_id(appointment_id)
        except Exception as e:
            print(e)
            return unhandled_error()
        
        return Response(response, status=200)