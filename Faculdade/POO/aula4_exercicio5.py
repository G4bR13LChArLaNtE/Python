'''Exercício 05

Importe o módulo abaixo para um programa
de teste e escreva testes unitários para
as funções do módulo:

def converte_para_celsius(fahrenheit):
    celsius = (5.0/9.0) * (fahrenheit - 32)
    return celsius


def converte_para_fahrenheit(celsius):
    fahrenheit = 1.8 * celsius + 32
    return fahrenheit

Utilize os valores abaixo como parâmetros
de entrada e saída das funções.

converte_para_fahrenheit(celsius)
Entrada
0
27

Saída
32.0
80.6




converte_para_celsius(fahrenheit)
Entrada
32
41

Saída
0
5.0
'''

from aula4_exercicio5_teste import converte_para_celsius
from aula4_exercicio5_teste import converte_para_fahrenheit


try:
    resultado = converte_para_celsius(32)
    assert resultado == 0
    print('Correto')
except AssertionError:
    print('Erro')

try:
    resultado = converte_para_celsius(41)
    assert resultado == 5.0
    print('Correto')
except AssertionError:
    print('Erro')

try:
    resultado = converte_para_fahrenheit(0)
    assert resultado == 32.0
    print('Correto')
except AssertionError:
    print('Erro')

try:
    resultado = converte_para_fahrenheit(27)
    assert resultado == 80.6
    print('Correto')
except AssertionError:
    print('Erro')
