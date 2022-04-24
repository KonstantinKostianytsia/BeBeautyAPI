import base64
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

def DecodeToken(token):
    token = str(token)
    token = token.split('.')
    result = base64.b64decode(str(token[1]))
    d = dict()
    result = str(result)
    result = result.replace("{"," ").replace(","," ").replace("}"," ").replace("'"," ").replace(":"," ").replace("\""," ")
    result = result.split()
    for i in range(1,len(result),2):
        d[result[i]] = result[i+1]
    return d

def get_tokens_for_user(user: User):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }