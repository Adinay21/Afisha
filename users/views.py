from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from users.serializers import UserRegisterSerializer, UserAuthSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


import random
from django.core.mail import send_mail
from django.conf import settings
from .models import ActivationCode



@api_view(['POST'])
def authorize_api_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']
    email = serializer.validated_data['email']
    user = authenticate(username=username, password=password, email=email)
    if user is not None:
        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)
        return Response(data={'key': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def register_api_view(request):
    serializer = UserRegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')
    email = serializer.validated_data.get('email')

    user = User.objects.create_user(username=username, password=password, email=email, is_active=False)

    activation_code = random.randint(100000, 999999)
    activation_code_str = str(activation_code)
    subject = "Ваш код активации"
    message = f"Ваш код активации для активации аккаунта: {activation_code_str}"
    from_email = settings.DEFAULT_FROM_EMAIL
    send_mail(subject, message, from_email, [email])
    ActivationCode.objects.create(user=user, code=activation_code_str)
    return Response(data={'user_id': user.id},
                    status=status.HTTP_201_CREATED)
