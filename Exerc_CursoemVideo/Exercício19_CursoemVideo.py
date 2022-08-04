#Exercício 19#

import random

N1 = input("Primeiro nome: ")
N2 = input("Segundo nome: ")
N3 = input("Terceiro nome: ")
N4 = input('Quarto nome: ')

lista = [N1, N2, N3, N4]

escolhido = random.choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))

