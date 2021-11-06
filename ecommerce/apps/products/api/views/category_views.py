from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from apps.products.api.serializer import CategorySerializer

#clase que contiene el CRUD de categoria
class CategoryViewSet(viewsets.GenericViewSet):
    serializer_class = CategorySerializer

    #obtendra todas las instancias que tenga el estado True
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    #obtendra solo una instancia por medio de un id y que su estado sea True
    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id = self.kwargs['pk'], state = True)

    #Metodo GET
    def list(self , request):
        #se guarda en una variable los datos de la instancia
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)

    #Metodo POST
    def create(self, request):
        #se guarda en una variable los datos que se obtienen en el body
        serializer = self.serializer_class(data = request.data)
        #se valida si el usuario es valido
        if serializer.is_valid():
            #de ser valido, se guardara
            serializer.save()
            #se retorna un mensaje y un estado 201 si la categoria es creada
            return Response({'message': 'Categoria registrada'}, status = status.HTTP_201_CREATED)
        #se retorna un mensaje con el error y un estado 400 si no se crea la categoria
        return Response({'error': serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

    #Metodo UPDATE
    def update(self, request, pk = None):
        #se verifica si la instancia existe
        if self.get_object().exists():
            #si existe se guarda en una variable la instancia y sus datos actualizados
            serializer = self.serializer_class(instance = self.get_object().get(), data = request.data)
            #se verifica si los datos son validos
            if serializer.is_valid():
                #de ser validos, se guardan
                serializer.save()
                #se retorna un mensaje y un estado 200 en caso de que se actualizen los datos
                return Response({'message':'Categoria actualizada'}, status = status.HTTP_200_OK)
        #se retorna un mensaje y un estado 400 en caso de que no se pueda actualizar los datos o si no se encontro la categoria
        return Response({'error': serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

    #Metodo DELETE
    def destroy(self, request, pk = None):
        #se verifica si la instancia existe
        if self.get_object().exists():
            #en caso de que exista se elimina
            self.get_object().get().delete()
            #se mretorna un mensaje y un estado 200 en caso de que la categoria es eliminada
            return Response({'message': 'Categoria eliminada'}, status = status.HTTP_200_OK)
        #se retorna un mensaje y un estado 400 en caso de que la categoria no se encuentre 
        return Response({'error': 'Categoria no encontrada'}, status = status.HTTP_400_BAD_REQUEST)
        