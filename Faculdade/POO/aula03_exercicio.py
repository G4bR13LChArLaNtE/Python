''' Exercício 01

Preencha um dicionário com as informações de 5 produtos.
-	Utilize o nome do produto como chave e o preço como valor. 
-	Solicite os dados ao usuário.
Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50.00

Exemplo:
Veja um exemplo da estrutura do dicionário.
{'Caneta': 3.0, 'Pen Drive': 100.0, 'Teclado': 30.0, 'Lápis': 1.50}
'''

produtos = { 'Caneta': 3.0, 'Pen Drive': 100.0, 'Teclado': 30.0, 'Lápis': 1.50, 'mouse': 20.0}
print(produtos)

for i in produtos:
    if produtos[i] > 50:
        print(produtos[i])

print()

'''Exercício 02

Preencha um dicionário com os dados de 5 alunos.
-	Utilize o ra do aluno como chave e uma lista de três notas como valor.
-	Solicite os dados ao usuário.
Percorra o dicionário e exiba a média de cada aluno.

Exemplo:
Veja um exemplo da estrutura do dicionário.
{1901502: [10, 8, 7.5], 2002441: [6, 5, 7.5], 2001332: [5, 8, 9.5]}
'''
notas = {2101478 : [7,8.5,9], 2102589: [5.5,6.7,4.1], 2102569: [3.1,4.5,9.5]}

for i in notas:
    print(i)
    soma = 0
    soma = notas[i][0] + notas[i][1] + notas[i][2] 
    md = soma/3
    print("O estudante de RA {} obteve a média {:.2f}".format(i, md))

print()

'''Exercício 03

Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada e o valor é a quantidade de vezes que essa vogal aparece no texto. 
A função deve receber o texto como entrada, e retornar o dicionário.

Exemplo:
Para o texto abaixo:
'faculdade de tecnologia impacta'

A função deve retornar o seguinte dicionário:
{'a': 5, 'u': 1, 'e': 3, 'o': 2, 'i': 2}

'''


frase = 'faculdade de tecnologia impacta'
letras = ['a', 'u', 'e', 'o', 'i']
q = []
n = 0
for i in range(5):
    n = letras[i]
    q.append(frase.count(n))

dic = {letras[0]:q[0], letras[1]:q[1], letras[2]:q[2], letras[3]:q[3], letras[4]:q[4]}

print(dic)

 


