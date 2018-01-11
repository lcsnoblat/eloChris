from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Elo(models.Model):
    nome = models.CharField(max_length=100)
    image =  models.CharField(max_length=1000)
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    comentario = models.CharField(max_length=1000)
    rank = models.IntegerField()

    def __str__(self):
        return self.nome

class PontosUsuario(models.Model):
    nome = models.CharField(max_length=100)
    pontos = models.IntegerField()
    elo = models.ForeignKey(Elo, related_name='elo_usuario')
    partidas_jogadas = models.IntegerField()
    partidas_ganhas = models.IntegerField()
    partidas_perdidas = models.IntegerField()

    def __str__(self):
        return self.nome