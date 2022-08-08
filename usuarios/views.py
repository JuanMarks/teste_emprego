from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from vagas.models import Vaga
from candidatos.models import Candidato
from .forms import TaskForm

# Create your views here.
def index(request):
    vagas = Vaga.objects.all()

    dados = {
        'vagas' : vagas
    }
    return render(request, 'index.html', dados)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['password']

        if email == "" or senha == "":
            print('Os campos email e senha nao podem ficar em branco')
            return redirect('login')
            
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                tipo_usuario = User.objects.filter(email=email).values_list('first_name', flat=True).get()
                auth.login(request,user)
                
                if tipo_usuario == 'USR':
                    return redirect('index')
                elif tipo_usuario == 'ADM':
                    return redirect('dashboard_empresa')
            
    return render(request, 'login.html')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip():
            print("O campo nome nao pode ficar em branco")
            return redirect('cadastro')
        
        if not email.strip():
            print("O campo email nao pode ficar em branco")
            return redirect('cadastro')
        
        if senha != senha2:
            print('As senhas nao estao iguais')
            return redirect('cadastro')
        
        if User.objects.filter(email=email).exists():
            print('usuario ja cadastrado')
            return redirect('cadastro')
        
        usuario1 = User.objects.create_user(username=nome, first_name='USR', email=email, password=senha) 
        usuario1.save()
        return redirect('login')
    else:
        return render(request, 'usuario/cadastro.html')
    

def logout(request):
    auth.logout(request)
    return redirect('index')

def cadastro_empresa(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']

        if not nome.strip():
            print("O campo nome nao pode ficar em branco")
            return redirect('cadastro_empresa')
        
        if not email.strip():
            print("O campo email nao pode ficar em branco")
            return redirect('cadastro_empresa')
        
        if User.objects.filter(email=email).exists():
            print('usuario ja cadastrado')
            return redirect('cadastro_empresa')

        usuario1 = User.objects.create_user(username=nome, first_name='ADM', email=email, password=senha) 
        usuario1.save()
        return redirect('login')
    else:
        return render(request, 'empresa/cadastro_empresa.html')
    
def dashboard_empresa(request):
    id = request.user.id
    vagas = Vaga.objects.filter(pessoa=id)

    dados = {
        'vagas' : vagas
    }
    return render(request, 'empresa/dashboard_empresa.html', dados)

def apagar_vaga(request, id):
    vaga = get_object_or_404(Vaga, pk=id)
    vaga.delete()
    return redirect('dashboard_empresa')

def editar_vaga(request, id):
    vaga = get_object_or_404(Vaga, pk=id)
    form = TaskForm(instance=vaga)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=vaga)

        if(form.is_valid()):
            vaga.save()
            return redirect('dashboard_empresa')
        else:
            return render(request, 'empresa/edittask.html', {'form': form, 'task': vaga})
    else:
        return render(request, 'empresa/edittask.html', {'form': form, 'task': vaga})

def saibamais(request, id):
    vaga = Vaga.objects.filter(id=id)
    
    dados = {
        'vagas' : vaga,
    }

    return render(request, 'saibamais.html', dados)

def cadastro_inscricao(request, id):
    if request.method == 'POST':
        nome_candidato = request.POST['nome']
        pretensao_salarial = request.POST['salarial']
        email = request.POST['email']
        escolaridade = request.POST['escolaridade']
        experiencia = request.POST['experiencia']
        vaga = Vaga.objects.filter(id=id)
        user = get_object_or_404(User, pk=request.user.id)
        vaga_nome = get_object_or_404(Vaga, pk=id)
        vaga_lista = Vaga()
        inscritos_na_vaga = Vaga.objects.filter(id=id).values_list('inscritos_na_vaga', flat=True).get()
        inscritos = [inscritos_na_vaga]
        if not Candidato.objects.filter(email=email).exists():
            candidato = Candidato.objects.create(pessoa=user, nome_candidato=nome_candidato, pretensao_salarial=pretensao_salarial, experiencia=experiencia, email=email, escolaridade=escolaridade, candidato_vaga=vaga_nome) 
            candidato.save()
            nome = Candidato.objects.filter(email=email).values_list('nome_candidato', flat=True).get()
            inscritos.append(nome)
            vaga.update(inscritos_na_vaga=inscritos)
        else:
            nome = Candidato.objects.filter(email=email).values_list('nome_candidato', flat=True).get()
            inscritos.append(nome)
            vaga.update(inscritos_na_vaga=inscritos)
            

        qtd_inscritos = Vaga.objects.filter(id=id).values_list('qtd_inscritos', flat=True).get()
        soma = qtd_inscritos + 1
        vaga.update(qtd_inscritos=soma)

        return redirect('index')
    else:   
        return render(request, 'usuario/formulario_inscricao.html')
    
    