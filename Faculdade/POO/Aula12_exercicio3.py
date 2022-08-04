
num1 = open('num_par.txt', 'r')

lista = []

for linha in num1:
    l1 = int(linha)
    lista.append(l1)

num2 = open('num_impar.txt', 'r')

for linha in num2:
    l2 = int(linha)
    lista.append(l2)

lista.sort()

print(lista)

num1.close()
num2.close()

num3 = open("num_ordem.txt", "w", encoding="utf-8")

for i in lista:
    num3.write(str(i) + '\n')

num3.close()
