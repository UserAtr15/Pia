from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from apps.orders.api.serializer import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    #se obtendra una instacia
    def get_queryset(self, pk = None):
        if pk is None:
            #se obtiene todas la instacias con estado True
            return self.get_serializer().Meta.model.objects.filter(state = True)
        #se obtiene una instacia expecifica por medio de un id y estado True
        return self.get_serializer().Meta.model.objects.filter(id= pk, state = True).first()
    
    #Metodo GET
    def list(self, request):
        #se guardan en una variable las instancias obtenidas
        order_serializer = self.get_serializer(self.get_queryset(), many = True)
        #retorna las instancias y un estado 200
        return Response(order_serializer.data, status= status.HTTP_200_OK)

    #Metodo POST
    def create(self, request):
        #se guarda los datos ingresados en el body
        serializer = self.serializer_class(data = request.data)
        #se verifica si los datos son validos
        if serializer.is_valid():
            #se guardan los datos
            serializer.save()
            #se retona un mensaje y un estado 201 en caso de que se crea el pedido
            return Response({'message': 'Pedido Creado'},status= status.HTTP_201_CREATED)
        #se retorna el error y un estado 400
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    #Metodo DELETE
    def destroy(self, request, pk =None):
        #se obtiene la instancia
        order = self.get_queryset().filter(id=pk).first()
        #si se encuentra la orden
        if order:
            #se cambia el estado del pedido
            order.state = False
            #se guarda el cambio
            order.save()
            #se retorna un mensaje y un estado 200
            return Response({'message': 'Eliminado'}, status = status.HTTP_200_OK)
        #se retorna un mensaje y un estado 400 
        return Response({'error':'No se encontro el pedido'}, status= status.HTTP_400_BAD_REQUEST)