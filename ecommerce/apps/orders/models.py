from django.db import models
from apps.base.models import BaseModel
from apps.users.models import User
from apps.products.models import Product

# Create your models here.

#Tabla Order
class Order (BaseModel):
    #atributo del usuario 
    order_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Pedido de usuario', null=True)
    #atributo de producto
    order_product = models.ManyToManyField(Product)
    #atributo de la direccion
    address = models.CharField('Direccion del pedido', max_length=255)
    #atributo de la hora 
    time = models.DateTimeField('Hora de Pedido', default='')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    