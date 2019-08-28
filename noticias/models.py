from django.db import models

# Create your models here.
class Escritor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{ self.apellido }, { self.nombre }"

class Articulo(models.Model):
    #autor = models.CharField(max_length=50)
    autor = models.ForeignKey(Escritor, on_delete=models.CASCADE, related_name='articulos')
    titulo = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=200)
    cuerpo = models.TextField()
    ubicacion = models.CharField(max_length = 120)
    fecha_publicacion = models.DateField()
    activo = models.BooleanField(default = True)
    fecha_creado = models.DateField(auto_now_add=True)
    fecha_actualizado = models.DateTimeField(auto_now =True)
    
    def __str__(self):
        return f"\'{ self.titulo }\' de { self.autor.nombre }"
    


