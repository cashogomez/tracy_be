from django.db import models
from perfiles.models import Perfil

# Create your models here.
class Log(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='logs')
    is_correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __sts__(self):
        return f"Log de {self.perfil.id}"