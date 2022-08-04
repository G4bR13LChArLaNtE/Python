n = int(input())


def entrada_dados(n, matriz_entrada):
    i = 0
    for i in range(n):
        linha = input()
        linha2 = linha.split(";")
        matriz_entrada.append(linha2)


def processamento_dados(n, matriz_entrada, sim, nao, n4):
    i = 0
    for i in range(n):
        n1 = int(matriz_entrada[i][1])
        n2 = float(matriz_entrada[i][2])
        if matriz_entrada[i][3] == "sim":
            n3 = (n2 + sim * (n1 / 1000))
        elif matriz_entrada[i][3] == "não":
            n3 = (n2 + nao * (n1 / 1000))
        n4.append(n3)


def saida_dados(matriz, n1, n):
    print('-----')
    print("BÔNUS")
    print("-----")
    i = 0
    for i in range(n):
        print("{}: R$ {:.2f}".format(matriz[i][0], n1[i]))



if 1 <= n <= 200:
    matriz_entrada = []
    n1 = []
    entrada_dados(n, matriz_entrada)
    sim = float(input())
    sim = round(sim, 4)
    nao = float(input())
    nao = round(nao, 4)
    processamento_dados(n, matriz_entrada, sim, nao, n1)
    saida_dados(matriz_entrada, n1, n)
