from app.serializer import CustomUserSerializer
from app.models import AuthVariant
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from app.exceptions import *
from django.contrib.auth import get_user_model

User = get_user_model()

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
    try:
        serializer = CustomUserSerializer(data=data.data)

        if serializer.is_valid(raise_exception = False) == False:
            #  raise SerializerNonValid
            pass

        user = User.objects.create_user(email = serializer.data["email"],auth_variant=serializer.data["auth_variant"],
                        first_name = serializer.data["first_name"], last_name = serializer.data["last_name"],
                        password="Test1234", username= serializer.data["email"] + "_" + serializer.data["auth_variant"]
                        )
        user.save()
    except Exception as e:
        print(e)

    return 

def check_unique_user_info(auth_variant: AuthVariant, email):

    if email is not None:
        obj = User.objects.filter(email = email, auth_variant = auth_variant)
        if len(obj) != 0:
            raise EmailIsExist


def check_is_user_exists(auth_variant: AuthVariant, email: str) -> User:
    print(auth_variant, email)
    obj = User.objects.filter(email = email, auth_variant = auth_variant)
    if len(obj) == 0:
        raise ObjectDoesNotExist
    return obj[0]
