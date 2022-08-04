'''Nesse programa temos vários exercícios feitos: 
Subtração de dois números;
Subtração de dois salários;
Cálculo de idade;
Cálculo da média de três notas.'''

n1 = int(input('Número 1:  '))
n2 = int(input('Número 2:  '))
sub = n1 - n2

print("\033[1;34m", 'A subtração de ', n1, '-', n2, "\033[1;31m" , 'é', sub, "\033[;1m")

a = 1045 #Salário mínimo em 2020
b = 1100 #Salário mínimo em 2021
c = b - a#Aumento do salário mínimo
print("O salário mínimo aumentou {} reais".format(c))

ano_atual = 2021
ano_nasc = int(input("Ano de nascimento: "))
idade = ano_atual - ano_nasc

if idade >= 21 and idade <= 29 :
    print("Você é um jovem adulto!")
elif idade >=30 and idade <= 40 :
    print("Você é um adulto!")
else:
    print("Você está na melhor idade! :)")
print("Sua idade é ", idade)

n3 = float(input("Digite a primeira nota: "))
n4 = float(input("Digite a segunda nota: "))
n5 = float(input("Digite a terceira nota: "))
md = (n3+n4+n5)/3
print("Sua média é {:.2f}".format(md))
