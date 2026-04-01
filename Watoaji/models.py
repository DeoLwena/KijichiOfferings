from django.db import models

# Create your models here.

class Mtoaji(models.Model):
    Hali_ya_Ushirika = [
        ('M',"Mshiriki"),
        ('S', "Sio_Mshiriki"),
    ]
    jina_la_kwanza = models.CharField(max_length=255, default='Hana')
    jina_la_mwisho = models.CharField(max_length=255, default='Jina')
    ushirika = models.CharField(choices=Hali_ya_Ushirika, default='M')
    namba_ya_ushirika = models.IntegerField(default=00)
    simu = models.CharField(null=True, max_length=15, blank=True)
    email = models.EmailField(null=True, blank=True)
    def __str__(self):
        return (self.jina_la_kwanza +' '+ self.jina_la_mwisho)