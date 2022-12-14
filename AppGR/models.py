from django.db import models

# Create your models here.

class Sombras(models.Model):
    codigo=models.IntegerField()
    color=models.CharField(max_length=100)
    tipo=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.codigo}, {self.color}, {self.tipo}'

class Base(models.Model):
    codigo=models.IntegerField()
    tono=models.CharField(max_length=100)
    cobertura=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.codigo}, {self.tono}, {self.cobertura}'

class Brochas(models.Model):
    numero=models.IntegerField()
    clase=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.numero}, {self.clase}'