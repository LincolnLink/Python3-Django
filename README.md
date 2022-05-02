# Python3-Django
Python 3 completo - programação com Django, PyQT5, Selenium, Regexp, Testes e TDD, POO, Design Patterns GoF, algoritmos.

python é interpretada.

# Usando: Virtualenv

- Se da bem melhor com o windows! 

- O comandode instalação de biblioteca de 3° deve ter "pip" antes.

- "pip install pymysql" 

- Se for o pipend deve por "pipenv" antes.

# Criando arquivo.

- Todo arquivo python é um modulo python.

- new python packt, uma pasta que cria um init.

- e bom que ajuda a importar modulos.

# Criando ambiente virtual (qualquer editor de texto)

- " -m venv env ".

- Depois de instalado deve ativar o ambiente virtual. 

- Para ativar o ambiente virtual deve executar o comando.

- "F:\GITHUB\Python3-Django\ProjetoDoZero>env\Scripts\activate.bat"

- Ativa executando o arquivo " activate.bat "

- Cria um arquivo, da extenção " .py " do modulo.

- Executa o comando " deactivate " para interromper o ambiente virtual.

# Python Basico.

### Comentarios

- Para digitar um comentario deve usar o "#"

# ----------- Estudando Django -----------------

### Instalando o Django

- Cria o projeto do zero.

- Comando:  " pip install django " 

- Comando para versão especifica: " pip install django==2.2.3 " 

- Comando para sair do terminar e deixar limpo: " exit ".

### Criando o PROJETO DJANGO!

- Comando que cria o projeto como CLI!

- " django-admin startproject 'NomeDoProjeto' ."

- Esse " . " no final serve para ele não criar mais pastas
uma dentro da outra!

- Na pasta projeto é gerados arquivos importantes.

- "settings.py" : Esse arquivo tem a configuração do que
foi instalado.

- "urls.py" : Nesse arquivo é configurado as URL.

- "wsgi.py" : Configura a parte de deploy.

- manage.py : ele que executa tudo.


### startando o projeto django.

- Comando que starta o projeto django(inicia um servidor local).

- " python manage.py runserver ".

- Rodar em outra porta: " python manage.py runserver 8888 ".

- " crt + c " para o servidor

### Criar um app (parte do FrontEnd)

- " python manage.py startapp 'NomeDoApp' "

- " python manage.py startapp AppFrontLincoln"

- Nesse projeto fica as views, informação de dados, etc.

<!--  ------------------- -->

### fazendo referencia do "front para o back"

- O app deve ser declarado no primeiro projeto.

- No arquivo "settings" do primeiro projeto, deve ser declarado
o caminho e nome do app criado, no array INSTALLED_APPS!

### Criando a url 

- No arquivo "urls.py" deve se configurar uma url para a tela que
for usar!

- Cria um arquivo com nome de urls.py na pasta do frontEnd.

- Começa importardo o 'include' do django.urls

- difine sua propria url padrão

<blockquete>
			
			from django.contrib import admin
			from django.urls import path, include

			urlpatterns = [
			    path('admin/', admin.site.urls),
			    path('AppFrontLincoln/', include('AppFrontLincoln.urls')),
			]

</blockquete>

### Criando uma view

- cria um metodo index na view

<blockquete>
	
			from django.urls import  path
			from django.http import  HttpResponse


			def index(request):
			    return  HttpResponse('Ola mundo!')

</blockquete>


- python manage.py makemigrations


- python manage.py migrate  



