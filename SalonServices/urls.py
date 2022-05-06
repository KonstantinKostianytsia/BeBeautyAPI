from django.urls import path
from .Views import salon_views


urlpatterns = [
    path('salons', salon_views.SalonView.as_view())
]