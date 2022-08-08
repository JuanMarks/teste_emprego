from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Vaga
# Create your views here.

def criar_vaga(request):
    if request.method == 'POST':
        nome_vaga = request.POST['nome_vaga']
        descricao = request.POST['descricao']
        vagas = request.POST['vagas']
        faixa_salarial = request.POST['faixa_salarial']
        escolaridade = request.POST['escolaridade']
        user = get_object_or_404(User, pk=request.user.id)
        vaga = Vaga.objects.create(
            pessoa=user, 
            nome_vaga=nome_vaga, 
            descricao_vaga=descricao, 
            qtd_vagas=vagas, 
            faixa_salarial=faixa_salarial,
            escolaridade=escolaridade, )
        vaga.save()
        return redirect('dashboard_empresa')
    else:
        return render(request, 'empresa/criar_vaga.html')



