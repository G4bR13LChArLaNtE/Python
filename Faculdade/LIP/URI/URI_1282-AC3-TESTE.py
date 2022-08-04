n = int(input())
matriz_entrada = []
n1 = []

if 1 <= n <= 200:
    i = 0
    for i in range(n):
        linha = input()
        linha2 = linha.split(";")
        matriz_entrada.append(linha2)
    i = 0
    sim = float(input())
    nao = float(input())
    for i in range(n):
        n2 = int(matriz_entrada[i][1])
        n3 = float(matriz_entrada[i][2])
        if matriz_entrada[i][3] == "sim":
            n4 = (sim * (n2/1000))
            n5 = n3 + n4
        elif matriz_entrada[i][3] == "não":
            n4 = (nao * (n2/1000))
            n5 = n3 +n4
        n1.append(n5)

    print('-----')
    print('BÔNUS')
    print('-----')
    i = 0
    for i in range(n):
        print("{}: R$ {}".format(str(matriz_entrada[i][0]), round(n1[i],3)))

