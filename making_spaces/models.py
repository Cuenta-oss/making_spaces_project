from django.db import models

class contactModel(models.Model):
    nombre = models.CharField(max_length=100) 
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    mensaje = models.TextField(max_length=300)
    
    class Meta:
        verbose_name = 'contactModel'
        verbose_name_plural = 'contactModels'
    
    def __str__(self):
        self.nombre
        