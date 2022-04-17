from rest_framework_simplejwt import views as jwt_views
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from app.Services import token_service, user_service
from django.core.exceptions import ValidationError
from app.check_permissions import required_permission, check_group_permission
from django.core.exceptions import ObjectDoesNotExist

class LoginView(jwt_views.TokenObtainPairView):
    '''
        login user
        required: 
            authorize_method: GOOGLE | FACEBOOK | APPLE

        for any user
    '''

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):

        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
        except TokenError:
            return Response("Not Authorized", status = 401)
        except ValidationError:
            return Response("User not found", status = 404)

        print(serializer.validated_data)
        user_service.save_refresh_token_in_cache(serializer.validated_data) # save refresh_token in server 

        return Response(serializer.validated_data, status = 200)     # send both tokens to client


class LogoutView(APIView):
    '''
        logout user
        required none
        for authenticated users
    '''
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        info = token_service.DecodeToken(request.META['HTTP_AUTHORIZATION'][8:-1])
        token_service.delete_refresh_token(info['user_id'])
        return Response("Success", status = 200)
        # delete tokens in client