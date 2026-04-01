from django.db import models
from Watoaji.models import Mtoaji
# Create your models here.
class Idara(models.Model):
    jina = models.CharField(max_length=255, default='Huduma za washiriki')
    def __str__(self):
        return self.jina


class Matoleo(models.Model):
    kiasi = models.DecimalField(max_digits=30,decimal_places=2)
    jina = models.ForeignKey('Watoaji.Mtoaji',on_delete=models.CASCADE)
    jina_la_idara = models.ForeignKey('Idara',on_delete=models.CASCADE)
    aina =models.CharField(max_length= 100, default="zaka")
    tarehe =models.DateTimeField(auto_now=True)

