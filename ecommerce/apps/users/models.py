from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):
    #Modelo para crear nuestro usuario
    def _create_user(self, username, email, name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        #se guarda el usuario
        user.save(using=self.db)
        return user

    #Funcion para crear un usuario
    def create_user(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, False, False, **extra_fields)

    #Funcion para crear un super usuario
    def create_superuser(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, True, True, **extra_fields)

#Clase Usuario
class User(AbstractBaseUser, PermissionsMixin):
    #Campo de el nombre de usuario con un maximo de 255 caracteres
    username = models.CharField(max_length = 255, unique = True)
    #Campo de email con un maximo de 255 caracteres
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    #Campo de el nombre del usuario con un maximo de 255 caracteres 
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    #Campo de el apellido del usuario con una maximo de 255 caracteres 
    lastname = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    #Campo de la imagen de usuario
    #image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
    #Campo donde se mostrara si el usuario esta activo o no
    is_active = models.BooleanField(default = True)
    #Campo donde se mostrara si el usuario es miembro
    is_staff = models.BooleanField(default = False)
    #Campo donde se guardara un registro del usuario
    historical = HistoricalRecords()
    objects = UserManager()

    #El verbose de como se mostrara en el admin
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name']

    def __str__(self):
        return f'{self.name} {self.lastname}'
