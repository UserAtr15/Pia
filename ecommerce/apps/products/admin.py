from django.contrib import admin
from apps.products.models import *
# Register your models here.

class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id','description')

admin.site.register(Category)
admin.site.register(Product)