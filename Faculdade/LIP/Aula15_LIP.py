nome, idade, peso = input().split()
print(nome)
print(idade)
print(peso)

def teste(a, b, c, d):
    print(f'a = {a} | b = {b} | c = {c} | d = {d}')





lista = [1, 2, 5, 7]
print(*lista)

teste(*lista)


#Busca:


lista2 = ['P', 'y', 't', 'h', 'o', 'n']
for item in lista2:
    print(item)

for key, value in enumerate(['P', 'Y', 'T', 'H', 'O', 'N']):
    print(key, value)


#Exercício 1:

def busca_linear(valor, lista):
    for i, item in enumerate(lista):
        if item == valor:
            return i

    return -1

n2 = 0
while n2 < 10:
    letra = input("Insira a letra procurada: ")
    print(busca_linear(letra,lista2))
    n2 += 1

#Exercício 2:

def busca_linear2(lista):
    for key, value in enumerate(lista):
        print(key, value)


busca_linear2(lista2)

