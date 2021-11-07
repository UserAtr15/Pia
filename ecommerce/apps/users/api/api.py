from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from apps.users.api.serializers import (UserSerializer, GetUserSerializer, UpdateUserSerializer)
from apps.users.models import User


class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = UserSerializer
    list_serializer_class = GetUserSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk = pk)
    
    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects\
                            .filter(is_active = True)\
                            .values('id','username', 'email', 'name')
        return self.queryset

    #Metodo Get
    def list(self, request):
        #se obtiene la instancia
        users = self.get_queryset()
        #se guarda los usuarios
        users_serializer = self.list_serializer_class(users, many = True)
        #retorna los datos del usuario y un 200
        return Response(users_serializer.data, status = status.HTTP_200_OK)

    #Metodo Post
    def create(self, request):
        #se obtienen los datos del body
        user_serializer = self.serializer_class(data=request.data)
        #se verifica si los datos son validos
        if user_serializer.is_valid():
            #se guardan los datos
            user_serializer.save()
            #retorna los datos guardados y un 201
            return Response(user_serializer.data, status = status.HTTP_201_CREATED)
        #retorna un mensaje y un 400
        return Response({'message': 'Error en el registro de usuario'}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk = None):
        #se obtiene una instancia por id
        user = self.get_object(pk)
        #se serializa
        user_serializer = self.serializer_class(user)
        #retorna los datos
        return Response(user_serializer.data)

    #Metodo UPDATE
    def update(self, request, pk=None):
        #se obtiene una instacia por id
        user = self.get_object(pk)
        #se obtienen los nuevos datos del body
        user_serializer = UpdateUserSerializer(user, data=request.data)
        #se verifican que sean validos
        if user_serializer.is_valid():
            #se guardan los datos
            user_serializer.save()
            #retorna los datos del usuario y un 200
            return Response(user_serializer.data,status=status.HTTP_200_OK)
        #retorna un mensaje y un 400
        return Response({'errors': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    #Metodo DELETE
    def destroy(self, request, pk = None):
        #se obtiene un instancia por id y se hace una eliminacion logica
        user_destroy = self.model.objects.filter(id=pk).update(is_active = False)
        if user_destroy == 1:
            #retorna un mensaje y un estado 200
            return Response({'message':'Usuario Eliminado'}, status=status.HTTP_200_OK)
        #retorna un mensaje y un 400
        return Response({'message':'El usuario no existe'}, status=status.HTTP_400_BAD_REQUEST)    

