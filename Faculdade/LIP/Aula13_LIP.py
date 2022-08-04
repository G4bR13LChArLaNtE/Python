#Exercício 1:

salarios2 = []
soma = 0
n1 = int(input("Quantos sálarios serão analizados? "))

for _ in range(n1):
    salario2 = float(input('Salário: R$ '))
    soma += salario2
    salarios2.append(salario2) #anexa ao final da própria lista um novo item

media = soma / n1

for salario2 in salarios2:
    if salario2 < media:
        print(f'Abaixo da média: R$ {salario2:.2f}')


# Exercício 2:
salarios = []
soma = 0
c = 0

while True:
    salario1 = float(input('Salário: R$ '))
    if salario1 != -1:
        salario = salario1
        soma += salario
        salarios.append(salario) #anexa ao final da própria lista um novo item
        c += 1
    elif salario1 == -1:
        break

media = soma / c

for salario in salarios:
    if salario < media:
        print(f'Abaixo da média: R$ {salario:.2f}')





# Exercício 3 - Dias da semana:

list_dias = ["Domingo", "segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado" ]
i = 0
for i in range(0,7,1):
    print(list_dias[i])



# Exercício 4 - Vogal:

nomes = []
i2 = 0
while i2 <= 4:
    nome = input("Digite o nome: ")
    nomes.append(nome) #anexa ao final da própria lista um novo item
    i2 += 1
q = 0
for nome in nomes:

    if (nome[0] == "A" or nome[0] == "E" or nome[0] == "I" or nome[0] == "O" or nome[0] == "U"):
        q += 1
print("A quantidade de nomes que começam com vogal é de {}".format(q))