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

# Tamanho padrão
# a variavel mais o valor deve ter 10 casas
num_3 = 158
print(f'{num_3:0>10}')
print(f'{num_3:0<10}')
print(f'{num_3:0^10}')

num_4 = 87.986
print(f'{num_4:.2f}')

num_5 = 79.986
print(f'{num_5:0>10.2f}')

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

# fazendo com metodos de string!

nome3 = nome2.ljust(20, '#')
print(nome3)
print(nome3.lower()) # tudo minusculo
print(nome3.upper()) # tudo maiusculo
print(nome3.title()) # primeiras letras maiuscula
