from django.db import models

# Create your models here.
class Articulo(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=200)
    cuerpo = models.TextField()
    ubicacion = models.CharField(max_length = 120)
    fecha_publicacion = models.DateField()
    activo = models.BooleanField(default = True)
    fecha_creado = models.DateField(auto_now_add=True)
    fecha_actualizado = models.DateTimeField(auto_now =True)
    
    def __str__(self):
        return f"{ self.autor } { self.titulo }"
    


