"""
Operadores Lógicos -

and, or, not
in , not in

"""

nome= 'Lincoln'

if 'n' in nome:
    print("Existe n no seu nome")
else:
    print("Não existe.")

# sistema completo

usuario = input('Nome de usuário: ')
senha = input('Senha do usário: ')

usuario_bd = 'luiz'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema!')
else:
    print('Usuairio ou senha inválidos.')
