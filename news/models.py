from django.db import models
from django.utils import timezone

# Create your models here.
class Noticia(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    creacion = models.DateTimeField(default=timezone.now)
    publicacion = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publicacion = timezone.now
        self.save()
    
    def __str__(self):
        return self.titulo
    
