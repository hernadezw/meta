from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


 # Modelos para modulo cliente 
class Departamento(models.Model):    
    nombre= models.CharField(max_length=250, null=False)
    status= models.BooleanField(default=True)
    create= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.nombre
    
class Municipio(models.Model):
    nombre= models.CharField(max_length=250, null=False)
    departamento= models.ForeignKey(Departamento, null=True, on_delete=models.CASCADE, related_name="deplist")
    status= models.BooleanField(default=True)
    create= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now_add=True)
    delete=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre



 


class TipoCliente(models.Model):
    
    nombre= models.CharField(max_length=250, null=False)
    status= models.BooleanField(default=True)
    create= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.nombre    
    
class Cliente(models.Model):
    AUTOCODE='CL'
    tipo_cliente=models.ForeignKey(TipoCliente, on_delete=models.CASCADE, related_name="clientelist", null=True)
    code = models.CharField(verbose_name="Code", max_length=10, unique=True, blank=True)
    nombre= models.CharField(max_length=250, null=False)
    apellido= models.CharField(max_length=250, null=False)
    nit=models.CharField(max_length=9)
    telefonoOne=models.CharField(max_length=12, null=False)
    telefonoTwo=models.CharField(max_length=12, null=True)
    email=models.CharField(max_length=250)    
    status= models.BooleanField(default=True)
    create= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    
    #class Meta:
       # unique_together =['tipo_cliente', 'nombre']
 
    
    def __str__(self):
        return self.nombre
    


class Direccion(models.Model):
    cliente=models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL, related_name="direccioncliente")
    calle= models.CharField(max_length=250)
    avenida= models.CharField(max_length=250)
    barrioColonia= models.CharField(max_length=250)
    zonaComunidad= models.CharField(max_length=250)
    numeroCasa= models.IntegerField()
    referencia=models.CharField(max_length=250)
    municipio= models.ForeignKey(Municipio, null=True, on_delete=models.SET_NULL, related_name="municipiolist")
    departamento=models.ForeignKey(Departamento, null=True, on_delete=models.SET_NULL, related_name="departamentolist")
    status= models.BooleanField(default=True)
    create= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return str( self.calle + " " + self.avenida) 

@receiver(post_save, sender = Cliente)
def set_auto_code(sender, instance, **kwargs):
    if kwargs.get('created'): # Entramos al if si se ha creado la instancia
        # Actualisamos la instancia
        sender.objects.filter(id = instance.id).update(code = instance.AUTOCODE + str(instance.id))