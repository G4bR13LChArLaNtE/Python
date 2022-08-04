''' Exercício 01
Preencha uma lista com 10 números digitados pelo usuário e exiba:
a) o maior número da lista
b) o menor número da lista
c) a quantidade de números pares contidos na lista
d) a média dos números contidos na lista
e) todos os números menores do que a média calculada no item anterior. '''

#Dados do programa:

lista1 = []
l1 = int(input("Digite o primeiro número: "))
lista1.append(l1)

#Processamento dos dados:

def inserir(lista1):
    i = 1
    for i in range(1,10,1):
        if i <= 9:
            n = int(input("Digite o próximo número: "))
            lista1.append(n)
        elif i == 10:
            n = int(input("Digite o último número: "))
            lista1.append(n)


inserir(lista1)

#Resposta a):

print("O maior número é: ",max(lista1))

#Resposta b):

print("O menor número é: ",min(lista1))

#Resposta c):

listapar = []
listaimpar = []

def pares_impares(lista1, par, impar):
    n = 0
    for i in range(10):
        if lista1[i] % 2 == 0:
            n = lista1[i]
            par.append(n)
        else:
            n = lista1[i]
            impar.append(n)
    return
pares_impares(lista1,listapar, listaimpar)
qpar = len(listapar)
qimpar = len(listaimpar)

print("A quantidade de números pares é:", qpar)
print("A quantidade de números impares é:", qimpar)

#Resposta d):
md = (sum(lista1)/10)
print("A média da lista é:", md)

#Resposta e):
lista2 = []
for i in range(10):
    if lista1[i] < md:
        n1 = lista1[i]
        lista2.append(n1)
        lista2.sort()
print("A lista de números menores que a média é: ", lista2)

''' Exercício 02
Preencha uma lista com 10 números digitados pelo usuário. A partir desta lista, gere uma lista com
os números pares e outra com os números ímpares.
Exemplo:
Suponha que a lista digitada seja: [1, 4, 7, 9, 5, 3, 7, 9, 8, 8].
Para esta lista, o programa deve gerar as seguintes listas:
[4, 8, 8]
[1, 7, 9, 5, 3, 7, 9] '''

#Resposta:

print("A lista com os números pares é: ", listapar)
print("A lista com os números impares é: ", listaimpar)

'''Exercício 03
Preencha duas tuplas com 5 números cada, informados pelo usuário. Concatene as duas tuplas e
exiba a tupla resultante.
Dica: primeiro crie duas listas, e então, converta as listas em tuplas utilizando a função tuple.
tupla = tuple(lista) # converte a lista em uma tupla
Exemplo: Suponha que as tuplas contenham os números:
(3, 1, 5, 3, 5)
(5, 5, 7, 3, 1).
Como resultado, o programa deve gerar a tupla:
(3, 1, 5, 3, 5, 5, 5, 7, 3, 1).
'''
#Dados do programa:

lista3 = []
lista4 = []

#Processamento dos dados:

def preencher(lista):
    n = 0
    for i in range(5):
        if i < 5:
            n = int(input("Digite o número: "))
            lista.append(n)
        else:
            return

preencher(lista3)
preencher(lista4)

tupla1 = tuple(lista3)
tupla2 = tuple(lista4)

tupla3 = tupla1 + tupla2

#Saída do dados:

print("Na tupla 1 temos os seguintes itens: ", tupla1)
print("Na tupla 2 temos seguintes itens: ", tupla2)

print("Na tupla 3, que é a soma das tuplas 1 e 2, temos seguintes itens: ", tupla3)


'''Exercício 04
Escreva uma função chamada intercala_numeros que recebe como entrada duas listas de três
elementos e retorna uma lista de seis elementos, com os números intercalados.
Exemplo: Suponha que as listas de entrada da função sejam:
[1, 2, 3]
[4, 5, 6]
Para estas listas, a função deve retornar:
[1, 4, 2, 5, 3, 6]
'''
#Dados do programa:

lista5 = [1,2,3]
lista6 = [4,5,6]
lista7 = []
#Processamento dos dados:

def intercala_numeros(lista1,lista2, lista3):
    for i in range(3):
        if i < 3:
            n1 = lista1[i]
            n2 = lista2[i]
            lista3.append(n1)
            lista3.append(n2)
    return

#Saída de dados:

intercala_numeros(lista5, lista6, lista7)
print("A lista 7 intercalada será: ", lista7)