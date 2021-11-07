from rest_framework import serializers
from apps.users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'lastname')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = '__all__'
    
    def create(self, validated_data):
        #se crea una variable que guardara la informacion registrada
        user = User(**validated_data)
        #la contraseña se encripta
        user.set_password(validated_data['password'])
        #se guarda el usuario
        user.save()
        return user

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'lastname')


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
    
    #funcion para los datos que se mostraran
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'name': instance['name'],
            'username': instance['username'],
            'email': instance['email']
        }