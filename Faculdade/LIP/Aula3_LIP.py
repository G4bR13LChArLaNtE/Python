# Crie um programa que receba dois números naturais e exiba uma
# mensagem indicando se o primeiro é divisível pelo segundo.

a = int(input('Primeiro: '))
b = int(input('Segundo: '))
print(f'{a} é divisível por {b}? {b != 0 and a % b == 0}') #O f no início do comando mostra que terá uma formatação especial

if b != 0 and a % b == 0:
    print("{} é divisível por {}".format(a,b))
else:
    print("Os números {} e {} não são divisíveis.".format(a,b))

#Escreva um programa em Python que receba
# do usuário 3 notas e calcule a média
# dessas notas. O programa deve imprimir
#"aprovado para média >= 6 ou "reprovado"
# se média for menor do que 6.

# opcional - adicione o número de faltas
    #o aluno pode ter 30 faltas

n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
ft = int(input("Digite as faltas: "))
media = (n1 + n2 + n3)/3

if (media >= 6) and ft < 29:
    print(f'Você tirou as seguintes notas {n1}, {n2} e {n3}, sua média é {media}; você acaba de ser aprovado!')
else:
    print('Você tirou as seguintes notas {:.2f}, {:.2f} e {:.2f}, sua média é {:.2f}; infelizmente você foi reprovado!'.format(n1, n2, n3, media))

print("Tenha um bom dia!")
