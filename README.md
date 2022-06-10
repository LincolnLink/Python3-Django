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

- Para comentar varias linhas se usa 3 aspas no inicio até o final da linha.
	

### Print

- sep: são parametros que recebe valor, para poder separar o texto.

- end: recebe um valor que é exibido no final.

- exemplo: 

<blockquete>

			print('824', '176', '070', sep='.', end='-18')

</blockquete>

### str - string

- São texto dentro de aspas, o python não é tipado, mas reconhece uma string.

- /n quebra a linha

- pode por aspas simples dentro de aspas dupla.

### 4 dados primitivos

- O python interpreta os dados.

- função type(): retorna o tipo do valor!

- pode converter o valor para outro, usando apenas o nome do tipo dele: int('14')

- 

<blockquete>

			Tipos de dados
			str - string - textos 'Assim' "Assim"
			int - inteiro - 123 0 -10
			float - real/ponto flutuante - 10.22
			bool - booleano/lógico - true/false 10== 10

			print (   type('Lincoln') )
			print (   type(4) )
			print (   type(4.58) )
			print (   type(True) )

			resposta: 
				<class 'str'>
				<class 'int'>
				<class 'float'>
				<class 'bool'>
			
</blockquete>

### 5 Aula Operador aritméticos

- se multiplica int com string, ele repete a strig o numero de vezes informado
no inteiro.

- srt() converte numero para string, não tem como concatenar numero.

- executa primeiro o do parentese.

- Lista de todos os operadores: 

https://docs.python.org/3/reference/expressions.html#operator-precedence

- prioridade: 

parenteses () -> 
exponenciação ** -> 
multiplicação/divisão/divisão inteira e modulo * // %
soma e subtração + -

<blockquete>

	+, -, *, /, %

    // -> arredonda a divizão

    ** -> potenciação

    % -> resto da divisão

    2 + 5 * 3 ** 2 - (23.5 + 23.5)

</blockquete>

### 6 Variaveis

- Iniciar com letra, pode conter números, separar "_",
letras minúsculas.

- A tipagem é dinamica.

### 7 Formatação de strings

- Exemplo para executar a string e os valores!

<blockquete>				

			nome = 'Lincoln'
			idade = 31
			peso = 80.564654654

			print(f'{nome } tem {idade} anos e o peso {peso:.2f}')
			print('O {2} tem a idade: {0} e o peso {1}'.format(idade, peso, nome))
			print('Nome: {n} ,Idade: {i}, Peso {p}'.format(i=idade, p=peso, n=nome))

</blockquete>

### 8 Exercicio e solução

-

### 9 Input

- Uma função que retorna uma texto, e recebe do usuario um valor, e transforma ele
em string, caso o valor seja numerico e seja feito um calculo com ele, precisa
 primeiro está convertendo para int ou float!

 - exemplo:

 <blockquete> 	

			nome = input("Qual o seu nome: ")
			idade = input("Qual a sua idade:  ")

			# print(f"O nome escrito foi : {nome}, com o tipo: ", f'{type(nome)}')
			print(f"O usuario {nome}, nasceu no ano de {2022 - int(idade)} ")

 </blockquete>


### 10 If, else e elif

- Só executa de acordo a condição.

<blockquete>

			if True:
			    print('Verdadeiro')
			else:
			    print('Não é verdadeiro.')

			if False:
			    print('Verdadeiro')
			elif True:
			    print('Agora é verdadeiro.')

</blockquete>

### 11 Operadores relacionais

- "== > >= < <= != ", exmplicou sobre os operadores

### 12 Operadores logicos

- "and, or, not" 

- in: 

- not in: 

- exemplo de um sistema simples:

<blockquete>			

		# sistema completo

		usuario = input('Nome de usuário: ')
		senha = input('Senha do usário: ')

		usuario_bd = 'luiz'
		senha_bd = '123456'

		if usuario_bd == usuario and senha_bd == senha:
		    print('Você está logado no sistema!')
		else:
		    print('Usuairio ou senha inválidos.')

</blockquete>

### 13 Quantidade de caracteres

 - igual o length do C#

<blockquete>

		usuario = input("digite seu usuario: ")
		qtd_caracteres = len(usuario)
		print(usuario, 'quantidade de caracteres:', qtd_caracteres, 'tipo: ', type(qtd_caracteres))

</blockquete>

### 14  Documentação - função que verifica o tipo!

- Documentação: https://docs.python.org/3/library/stdtypes.html

- isnumeric, isdigit, isdecimal

- tratamento de erro alternativo:

https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py

- Tratamento de erro com try/except

### 15 Pass e Elipsis

- Pass: é um codigo que declara como se fosse um block sem nada, ele eita o erro, block esse que pode ficar em um if ou else, indica que algum codigo ainda vai ser desenvolvido ali.

- pass: é com 'p' minusculo! 

- Elipsis tem o mesmo efeito mas não foi feito para isso, para usar elipsis basta por '...', tres pontos sem as aspas.

<blockquete>

			valor = True
			if valor:
			    pass
			else:
			    print('Tchau')

</blockquete>

### 16 Exercicio!

- video 30 é um exercicio e o 31 é o resultado do exercicio

### 17 Formatando valores(arredondando)

- Arredondando com Format()

<blockquete>

			"""
			Formatando valores com modificadores


			:s - Texto(string)
			:d - Inteiros(int)
			:f - Números de ponto flutuante (float)
			:.(NÚMERO)f - Quantidade de casas decimais (float)
			:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

			> - Esquerda
			< - Direita
			^ - Centro

			"""
			num_1 = 10
			num_2 = 3
			divisao = num_1 / num_2
			print('{:.2f}'.format(divisao))
			print(f'{divisao:.2f}')

</blockquete>

- Definindo um tamanho padrão

<blockquete>

			num_3 = 158
			print(f'{num_3:0>10}')
			print(f'{num_3:0<10}')
			print(f'{num_3:0^10}')

			num_4 = 87.986
			print(f'{num_4:.2f}')

			num_5 = 79.986
			print(f'{num_5:0>10.2f}')

</blockquete>

- Formatando texto

<blockquete>

			nome = 'Lincoln Ferreira'
			print(f'{nome:#^50}')

			nome_formatado = '{:@>50}'.format(nome)
			print(nome_formatado)
			nome_formatado = '{:@>14}'.format(nome)
			print(nome_formatado)


			nome_formatado = '{n:@>20}'.format(n=nome)
			print(nome_formatado)

			nome2 = 'linColn'
			sobrenome = 'Ferreira'
			nome_formatado2 = '{0:$^20} {1:#^20}'.format(nome2, sobrenome)
			print(nome_formatado2)

</blockquete>

- Formatando texto com função de string

<blockquete>

			nome3 = nome2.ljust(20, '#')
			print(nome3)
			print(nome3.lower()) # tudo minusculo
			print(nome3.upper()) # tudo maiusculo
			print(nome3.title()) # primeiras letras maiuscula

</blockquete>



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





<blockquete>

	

</blockquete>
