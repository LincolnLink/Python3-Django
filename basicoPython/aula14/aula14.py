"""
Documentação!
Funções que verifica se pode ser convertido para numerico ou decimal ou digito.
Tratamento de erro!
Tratamento de erro alternativo!
"""
num1 = input('Digite um número: ')
num2 = input('Digite um número: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('ERROR')


"""Alternativa para tratar o erro, codigo avançado!"""

import re

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


###########
#  USAGE  #
###########

# Float
print(is_float('-101.0112'))  # True
# Int
print(is_int('-1010112'))  # True
# Numbers in general (float ou int)
print(is_number('-1010.112'))  # True

# False
print(is_number('123a'))  # False


