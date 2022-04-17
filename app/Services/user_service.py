import os
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from app.exceptions import *

def get_user_info(user_id):
    #user_id = required_permission(request, "auth.view_user")
    user = User.objects.get(id = user_id)
    return {
        "id": user.id,
        "username" : user.username,
        "first_name" : user.first_name,
        "last_name" : user.last_name,
        "email" : user.email, 
    }

def register_user(data):
    serializer = UserSerializer(data = data )

    if serializer.is_valid(raise_exception = True) == False:
         raise SerializerNonValid
    try:
        check_unique_user_info(username = serializer.data['username'],
                           email = serializer.data['email'])
    except EmailIsExist:
        raise EmailIsExist
    except UsernameIsExist:
        raise UsernameIsExist

    user = User.objects.create_user(username = serializer.data["username"], email = serializer.data["email"], password = serializer.data["password"],
                             first_name = serializer.data["first_name"], last_name = serializer.data["last_name"])
    user.groups.set([1]) # client group
    user.save()

    
    return 

def check_unique_user_info(username = None , email = None):

    if email  is not None:
        obj = User.objects.filter(email = email)
        if len(obj) != 0:
            raise EmailIsExist

    if username is not None:
        obj = User.objects.filter(username = username)
        if len(obj) != 0:
            raise UsernameIsExist