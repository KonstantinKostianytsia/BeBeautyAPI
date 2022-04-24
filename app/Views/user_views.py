from app.models import CustomUser
from app.Services.error_handler import handle_error, unhandled_error
from rest_framework_simplejwt import views as jwt_views
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from app.Services import token_service, user_service
from django.core.exceptions import ValidationError
from app.check_permissions import required_permission, check_group_permission
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginView(APIView):
    '''
        login user
        required: 
            authorize_method: GOOGLE | FACEBOOK | APPLE
            email: string
        for any user
    '''

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):

        try:
            auth_variant = request.data["auth_variant"]
            email = request.data["email"]
            user = user_service.check_is_user_exists(auth_variant,email)

        except ObjectDoesNotExist:
            return handle_error("Not Found user", "NOT_FOUND_USER", 404)
        except Exception as e:
            print(e)
            return unhandled_error()  

        return Response(token_service.get_tokens_for_user(user), status = 200)     # send both tokens to client

class CreateUserView(APIView):
    '''
        create user if login returns error
        required: 
            auth_variant: GOOGLE | FACEBOOK | APPLE
            first_name: str
            last_name: str
            email: str
        for any user
    '''

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            auth_variant = request.data['auth_variant']
            email = request.data['email']
            user_service.check_is_user_exists(auth_variant,email)

            return handle_error("Already exists", "USER_ALREADY_EXISTS", 400)

        except ObjectDoesNotExist:
            user_service.register_user(request)
            return Response(None, status = 201)
        except:
            return unhandled_error()  


class LogoutView(APIView):
    '''
        logout user
        required none
        for authenticated users
    '''
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        info = token_service.DecodeToken(request.META['HTTP_AUTHORIZATION'][8:-1])
        # token_service.delete_refresh_token(info['user_id'])
        return Response("Success", status = 200)
        # delete tokens in client