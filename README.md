# INSTRUÇÕES
 Primeiro com a pasta aberta no vscode faça para ativar a maquina virtual
 
 ```bash
 ./venv/Scripts/activate 
 # ou 
 source ./venv/Scripts/activate
 # com a venv ativada ligue o servidor
 python manage.py runserver
 
 ```
 
 ##	ADMs ou Empresas(ADM)
```
 nome de usuario = juan (django admin)
 email = juan@gmail.com 
 senha = 123456
	
 email = teste@gmail.com
 senha = 123456
```
## Usuarios comuns(USR)
```
nome de usuario = juanito
email = juanito@gmail.com
senha = 123456
	
nome de usuario = teste1
email = teste1@gmail.com
senha = 123456
```

<p>So da pra fazer login com email, menos no django admin que so da pra fazer login com o nome de usuario</p>
<p>So quem pode criar vagas sao os adms ou empresas e so quem pode se inscrever na vagas são os usuarios </p>
<p>Para as empresas existe um dashboard onde poderam editar ou apagar as vagas que elas criaram</p>
<p>Na dashboard da empresa nao mostrara vagas criadas por outras empresas</p>
<p>Para os usuarios somente a pagina principal de vagas mas o botao de se inscrever desaparece se o usuario ja estiver inscrito na vaga </p>
<p>OBS: Quando o usuario se inscrever na vaga no campo Seu Nome coloque o nome de usuario </p>
<p>Existe uma pagina saiba mais ou read more onde as empresas e os usuarios poderam acessar mas existe um campo que somente as empresas irao ver, que é o inscritos na vaga </p>
