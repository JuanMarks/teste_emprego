from django.db import models
from django.contrib.auth.models import User
from vagas.models import Vaga
# Create your models here.

class Candidato(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_candidato = models.CharField(max_length=30)
    email = models.EmailField()
    pretensao_salarial = models.IntegerField()
    experiencia = models.CharField(max_length=100)
    escolaridade = models.CharField(max_length=100)
    candidato_vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_candidato