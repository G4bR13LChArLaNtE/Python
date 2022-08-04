'''Exercício 01
Nesta questão você deve identificar as partes
problemáticas do código e reescrevê-lo
utilizando tratamento de exceções.
Ou seja, devem ser identificadas todas
as exceções que podem ser geradas e,
para cada uma, deve ser dado o
tratamento adequado que, nesse exercício,
significa alertar o usuário quanto ao problema.

x = int(input('Primeiro valor:'))
y = int(input('Segundo valor:'))
z = x / y
print('O resultado da divisão é:', z)
'''

while True:
    try:
        x = int(input('Primeiro valor:'))
        y = int(input('Segundo valor:'))
        z = x/y
        print('O resultado da divisão é:', z)
    except ZeroDivisionError:
        print('Não é possível didvidir um número por zero.')
        break
    except ValueError:
        print('O primeiro ou segundo número não é inteiro.')
        break

'''Exercício 02
O código abaixo lança uma exceção e interrompe
a execução do programa.
Utilizando tratamento de exceções, corrija
o programa com o objetivo de alertar o usuário sobre o
erro ocorrido, e impedir que o programa seja interrompido bruscamente.

def funcao_1():
    print('Início da função')
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(15):
        print(lista[i])
    print('Fim da função')

print('Início do programa')
funcao_1()
print('Fim do programa')
'''


def funcao_1():
    print('Início da função')
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        for i in range(15):
            print(lista[i])
    except IndexError:
        print('Erro de indexação no programa.')

        print('Fim da função')


print('Início do programa')
funcao_1()
print('Fim do programa')

'''Exercício 03
Preencha uma lista com 5 nomes de pessoas, informados pelo usuário.
a)Criar uma função que recebe como parâmetro de
entrada a lista e uma posição (índice) dessa lista e
retorna o nome que está nessa posição.
Essa função deve gerar e tratar uma exceção do
tipo IndexError caso o índice não exista na lista.
'''


def recebe(lista):
    n = str(input("Digite o primeiro nome:"))
    lista.append(n)
    for i in range(1, 5, 1):
        n = str(input("Digite o próximo nome: "))
        lista.append(n)
    return lista


def retorna(lista, pos):
    pos = 0
    pos = int(input("Digite o indice desejado: "))
    try:
        print("O nome contido na posição {} é {}.".format(pos, lista[pos]))
    except IndexError:
        print("Houve um erro no indice digitado, não existe esse indice,")
        print("tente outra vez.")


pos = 0
lista = []
recebe(lista)
retorna(lista, pos)


'''Exercício 04
Crie um dicionário para armazenar uma listagem de alunos.
a)Utilize como chave o RA do aluno e como valor o nome do aluno.
b)Os dados devem ser informados pelo usuário
c)O RA de cada aluno deve ser composto por um
número inteiro de exatamente 7 dígitos.
-Caso o RA informado não esteja no formato correto, deve
ser gerada uma exceção do tipo ValueError
-Caso o RA informado já exista no dicionário, deve
ser gerada uma exceção do tipo TypeError

Observação: Você pode utilizar o código abaixo como exemplo e
alterá-lo para gerar e tratar as exceções solicitadas.
alunos = {}
for i in range(5):
    ra = int(input('RA: '))
    nome = input('Nome: ')
    alunos[ra] = nome
print(alunos)
'''

alunos = {}
for i in range(5):
    try:
        ra = int(input('RA: '))
        if len(str(ra)) != 7:
            raise ValueError
        if ra in alunos:
            raise TypeError
        nome = input('Nome: ')
        alunos[ra] = nome
    except ValueError:
        print('Digite o RA corretamente.')
    except TypeError:
        print('Já temos esse aluno cadastrado.')
print(alunos)

