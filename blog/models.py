from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=250)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo
    
