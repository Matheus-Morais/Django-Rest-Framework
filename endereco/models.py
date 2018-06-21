from django.db import models

# Create your models here.

class Endereco(models.Model):
    estado = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    rua = models.CharField(max_length=150)
    complemento = models.CharField(max_length=150, null=True, blank=True)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.cidade
