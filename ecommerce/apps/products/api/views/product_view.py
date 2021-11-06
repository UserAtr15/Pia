from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from apps.products.api.serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    #obtendra las instancias
    def get_queryset(self, pk=None):
        #obtiene todas las instancias con un estado True
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        #obtiene una instancia expecifica por medio de id y de estado True
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    #Metodo GET
    def list(self, request):
        #se guarda en una variable las instancias
        product_serializer = self.get_serializer(self.get_queryset(), many = True)
        #retorna las instancias y un estado 200
        return Response(product_serializer.data, status = status.HTTP_200_OK)

    #Metodo POST
    def create(self, request):
        #se guarda en una variable los datos ingresados en el body
        serializer = self.serializer_class(data = request.data)
        #se verifican si los datos son validos
        if serializer.is_valid():
            #se guardan los datos
            serializer.save()
            #se retorna un mensaje y un estado 201 en caso de que se crea
            return Response({'message': 'Producto Creado'},status = status.HTTP_201_CREATED)
        #se retorna un mensaje y un estado 400 en caso de haber un error
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    #Metodo UPDATE
    def update(self, request, pk = None):
        #se obtiene la instacia
        if self.get_queryset(pk):
            #se guarda en una variable los datos actualizados
            product_serializer = self.serializer_class(self.get_queryset(pk), data =  request.data)
            #se valida los datos actualizados
            if product_serializer.is_valid():
                #se guardan los datos
                product_serializer.save()
                # se retorna los datos y un estado 200
                return Response(product_serializer.data, status = status.HTTP_200_OK)
        #se retorna el error y un estado 400
        return Response(product_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    #Metodo DELETE
    def destroy(self, request, pk = None):
        #se obtiene la instacia
        product = self.get_queryset().filter(id = pk).first()
        #si se encuentra el producto
        if product:
            #cambia el estado del producto a falso
            product.state = False
            #guarda el cambio
            product.save()
            #retorna un mensaje y un estado 200
            return Response({'message': 'Eliminado'}, status = status.HTTP_200_OK)
        #retorna un mensaje y un estado 400
        return Response({'error': 'El producto no existe'}, status = status.HTTP_400_BAD_REQUEST)