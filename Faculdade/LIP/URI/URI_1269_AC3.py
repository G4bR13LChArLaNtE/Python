import copy
linha = input()
linha1 = linha.split()
for f in range(len(linha1)):
    linha1[f] = int(linha1[f])
linha3 = linha1
linha3.sort()

def opcaos(linha1, linha3):
    i = 0
    j = 0
    a = 0

    linha2 = []
    linha2.append(linha1)

    while True:
        linhas= input().split()

        if linhas[0] == "adicionar":
            linhas[1] = int(linhas[1])
            linha1.append(linhas[1])
            linha2[j] = linha1
            for f in range(len(linha2[j])):
                linha2[j][f] = int(linha2[j][f])
            linha2[j].sort()



        elif linhas[0] == "remover":
            linhas[1] = int(linhas[1])
            linha1.remove(linhas[1])
            linha2[j] = linha1
            for f in range(len(linha2[j])):
                linha2[j][f] = int(linha2[j][f])
            linha2[j].sort()



        elif linhas[0] == "exibir":
            j += 1
            linha4 = []
            linha4 = list.copy(linha1)
            linha2.append(linha4)
            for f in range(len(linha2[j])):
                linha2[j][f] = int(linha2[j][f])
                linha2[j].sort()
            linha2[j].append(linha2)


        elif linhas[0] == "encerrar":

            print(linha)

            print(linha2)

            break


opcaos(linha1, linha3)

