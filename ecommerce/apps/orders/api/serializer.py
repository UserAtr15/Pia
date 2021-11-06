from django.db.models.fields import SlugField
from rest_framework import fields, serializers
from apps.orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    #se usa slugrelatedfield para mostrar los productos
    order_product = serializers.SlugRelatedField(many = True, read_only = True, slug_field='name')
    #se usa stringrelatedfield para mostrar el usuario
    order_user = serializers.StringRelatedField()
    #se utiliza datetimefield para mostrar la fecha y hora
    time = serializers.DateTimeField()

    class Meta:
        model = Order
        fields = [ 'id','order_user', 'order_product','address','time']


    
