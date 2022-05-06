from django.contrib import admin
from django.urls import path, include

from .Views import user_views

urlpatterns = [
    # path('registr/', user_views.RegistrUserView.as_view() ), # +
    path('login', user_views.LoginView.as_view()), # +
    path('create_user', user_views.CreateUserView.as_view()),
    # path('refresh/',user_views.RefreshAccessTokenView.as_view() ), # ?
    # path('user_info/', user_views.UserInfoView.as_view()), # +
    path('logout', user_views.LogoutView.as_view()), # + need to make autorefresh

]