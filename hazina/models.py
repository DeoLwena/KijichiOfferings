from django.db import models

# Create your models here.
class Mtoaji(models.Model):
    jina_la_kwanza = models.CharField(max_length=255, default='john')
    jina_la_mwisho = models.CharField(max_length=255, default='doe')
    ushirika = models.CharField(max_length=255, default='sio mshiriki')
    namba_ya_ushirika = models.IntegerField(default=00)
    simu = models.FloatField(null=True, max_length=15)
    email = models.EmailField(null=True)


class Idara(models.Model):
    idara = models.CharField(max_length=255)

class Ainayamatoleo(models.Model):
    AINAZAMATOLEO=[('Z','Zaka'),('S','Sadaka'),('I','Idara'),('M','Matoleo mengine')]
    aina = models.CharField(max_length=20,choices=AINAZAMATOLEO, default='I')

class Matoleo(models.Model):
    kiasi = models.DecimalField(max_digits=30,decimal_places=2)
    mtoaji = models.ForeignKey(Mtoaji,on_delete=models.CASCADE)
    idara = models.ForeignKey(Idara,on_delete=models.CASCADE)
    ainayamatoleo =models.ForeignKey(Ainayamatoleo, on_delete=models.CASCADE)


