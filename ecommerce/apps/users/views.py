from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.users.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users.api.serializers import (CustomTokenObtainPairSerializer, CustomUserSerializer)

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request):
        username = request.data.get('username','')
        password = request.data.get('password','')
        user = authenticate(username = username, password = password)

        if user:
            login_serializer = self.serializer_class(data = request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesion'
                }, status = status.HTTP_200_OK)
            return Response({'error': 'Usuario o contraseña incorrecto'},status = status.HTTP_400_BAD_REQUEST)

class Logout(GenericAPIView):
    def post(self, request):
        user = User.objects.filter(id = request.data.get('user',0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesion terminada'}, status = status.HTTP_200_OK)
        return Response({'error':'Error'}, status=status.HTTP_400_BAD_REQUEST)