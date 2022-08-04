lista = []
i = 0
valor = 0
soma = 0
n1 = 0
def imprime(i, lista, soma):
    valor2 = 0
    media = soma/i
    print("MEDIA: {:.2f}".format(media))
    for j in range(0,i):
        valor2 = lista[j]
        if valor2 < media:
            print(lista[j])

while True:
    soma += valor
    valor = int(input())
    if valor < 0:
        break
    lista.append(valor)
    i += 1

imprime(i, lista, soma)

