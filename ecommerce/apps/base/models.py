from django.db import models

# Create your models here.
class BaseModel(models.Model):
    #atributo id del modelo base
    id= models.AutoField(primary_key= True)
    #atributo estado del modelo base
    state = models.BooleanField('Estado', default = True)

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'