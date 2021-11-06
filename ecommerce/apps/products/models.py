from django.db import models
from apps.base.models import BaseModel
# Create your models here.

#Tabla Categoria
class Category (BaseModel):
    #atributo nombre
    name = models.CharField('Nombre de Categoria', max_length= 100, unique=True, null= True, blank= True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.name

#Tabla Producto
class Product(BaseModel):
    #atributo nombre
    name = models.CharField('Nombre de Producto', max_length= 50, unique= True, null= False, blank= False)
    #atributo descripcion
    description = models.CharField('Descripcion', max_length= 100, unique=True, null= False, blank= False)
    #atributo imagen
    image = models.ImageField('Imagen del Producto', upload_to ='products/', null = True, blank = True)
    #llave foranea con cateogria
    category_product = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name= 'Categoria de Producto', null=True)
    
    class Meta:

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.name