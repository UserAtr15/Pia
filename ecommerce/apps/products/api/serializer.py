from rest_framework import serializers
from apps.products.models import Product
from apps.products.models import Category

class ProductSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Product
        exclude = ('state', 'image')
    
    #muestra los datos
    def to_representation(self, instance):
        return {
             'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            #'image': instance.image if instance.image != '' else '',
            'category_product': instance.category_product.name if instance.category_product is not None else ''
        }

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']