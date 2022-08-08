
from django import forms

from vagas.models import Vaga

class TaskForm(forms.ModelForm):

    class Meta:
        model = Vaga
        fields = (
                'nome_vaga', 
                'descricao_vaga',
                'qtd_vagas',
                'faixa_salarial',
                'escolaridade')