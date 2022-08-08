from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
#from candidatos.models import Candidato
# Create your models here.

class Vaga(models.Model):
    salarial = (
        ('Até 1000','Até 1000'),
        ('de 1000 a 2000','de 1000 a 2000'),
        ('de 2000 a 3000','de 2000 a 3000'),
        ('Acima de 3000','Acima de 3000')
    )

    escolaridade_list = (
        ('Ensino fundamental', 'Ensino fundamental'),
        ('Ensino médio', 'Ensino médio'),
        ('Tecnólogo', 'Tecnólogo'),
        ('Ensino Superior', 'Ensino Superior'),
        ('Pós / MBA / Mestrado', 'Pós / MBA / Mestrado'),
        ('Doutorado', 'Doutorado')
    )
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_vaga = models.CharField(max_length=70)
    descricao_vaga = models.TextField()
    date = models.DateField(default=datetime.now, blank=True)
    qtd_vagas = models.IntegerField(default=0)
    faixa_salarial = models.CharField(max_length=50, choices=salarial)
    escolaridade = models.CharField( max_length=40 , choices=escolaridade_list)
    inscritos_na_vaga = models.CharField(max_length=100)
    qtd_inscritos = models.IntegerField(default=0)
    #candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome_vaga

    
    
