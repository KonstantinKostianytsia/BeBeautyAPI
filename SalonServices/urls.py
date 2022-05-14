from django.urls import path
from .Views import salon_views


urlpatterns = [
    path('salons/employees/skills', salon_views.GetEmployeesServices.as_view()),
    path('salons/employees/available_slots', salon_views.EmployeesSlots.as_view()),
    path('salons/employees', salon_views.GetEmployee.as_view()),
    path('salons', salon_views.SalonView.as_view()),
    path('config', salon_views.GetConfigInfo.as_view()),
]