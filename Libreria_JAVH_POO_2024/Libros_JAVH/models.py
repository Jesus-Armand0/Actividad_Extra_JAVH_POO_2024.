from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=14)
    imagen = models.ImageField(upload_to='libros_imagenes/', blank=True, null=True)

    def __str__(self):
        return self.titulo
# Create your models here.
