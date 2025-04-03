from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    #dejar a los susuarios escojer si agregar o no una tarea
    description = models.TextField(blank=True)
    
    #estos datos no se muestran como tal asi que no se pediran
    #controla si la tarea esta completa o no
    is_completed = models.BooleanField(default=False)
    #para tener las fechas de cuando las registremos
    created = models.DateTimeField(auto_now_add=True)
    
    #se crea para tener un orden en la base de datos
    class Meta:
        #ordena de mandera descendente por la fecha de creacion
        ordering = ['-created']
    #ver la tarea que estamos haciendo
    def __str__(self):
        return self.title