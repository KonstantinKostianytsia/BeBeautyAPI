import datetime
import os
from app.Services.error_handler import handle_error, unhandled_error
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from SalonServices.Services import salon_services, employee_service
from app.Services import token_service

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

class GetEmployee(APIView):
    '''
        return salons employees
        required:
            salon_id: int
    '''

    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        try:
            salon_id = int(request.GET.get("salon_id"))
            response = []
            if(salon_id):
                response = employee_service.get_employees_by_salon_id(salon_id)

        except Exception as e:
            print(e)
            return unhandled_error()
        
        return Response(response, status=200)
    

class GetEmployeesServices(APIView):
    '''
        return employees services
        required:
            employee_id: int
    '''

    permission_classes = (AllowAny,)

    def get(self,request):
        try:
            employee_id =int(request.GET.get("employee_id"))
            response = []
            if(employee_id):
                response = employee_service.get_employee_skills(employee_id)
        except Exception as e:
            print(e)
            return unhandled_error()
        
        return Response(response, status=200)

class EmployeesSlots(APIView):
    '''
        return employees booked slots for date
        required:
            employee_id: int
            date: Date,
    '''

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            employee_id =int(request.GET.get("employee_id"))
            date = datetime.datetime.strptime(request.GET.get("date"), '%Y-%m-%d')
            response = []
            if(employee_id == None):
                return handle_error("Required field is missed", "REQUIRED_FIELD_MISSED", 400)
            employees_appointments = employee_service.get_employee_appointments(employee_id, date)
            for appointment in employees_appointments:
                response.append({
                    'start_date': appointment["start_date"],
                    'end_date': appointment['end_date'],
                })
        except Exception as e:
            print(e)
            return unhandled_error()
        
        return Response(response, status=200)

    '''
        creates appointment 
        required:
            employee_id: int
            start_date: Date
            end_date: Date
            services_ids: string
    '''
    def post(self, request):
        try:
            print(request.headers)
            token = request.headers['Authorization'][7:]
            token_info = token_service.DecodeToken(token)
            message = salon_services.create_appointment(token_info["user_id"],request.data)
        except Exception as e:
            print(e)
            return unhandled_error()
        return Response(message, status=201)
        

class UserAppointments(APIView):
    '''
        return user appointments
    '''

    permission_classes = (IsAuthenticated,)
    
    def get(self,request):
        try:
            token = request.headers['Authorization'][7:]
            token_info = token_service.DecodeToken(token)
            appointments = salon_services.get_user_appointments(token_info["user_id"])
        except Exception as e:
            print(e)
            return unhandled_error()
        
        return Response(appointments)
        


class GetConfigInfo(APIView):
    '''
        return config info
    '''

    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            response = {}
            response["WORK_DAY_BEGGINING"] = int(os.getenv('WORK_DAY_BEGGINING', 9))
            response["WORK_DAY_END"] = int(os.getenv('WORK_DAY_END', 18))
            response["APPOINTMENT_BOOK_STEP"] = int(os.getenv("APPOINTMENT_BOOK_STEP", 30))
        except Exception as e:
            return unhandled_error()

        return Response(response, status=200)
