n = int(input())
notas_ant = []
notas_dep = []
notas_aux = []
n1 = 0
def nota_n(n, notas_n):
    for i in range(n):
        n1 = float(input())
        if n1 <= 10:
            notas_n.append(n1)


def compare(n, notas1, notas2, notas3, n1):
    for i in range(n):
        if notas1[i] == notas2[i]:
            notas3.append("-")
        else:
            notas3.append("*")
            n1 += 1

    return (n1)

def imprima(n, notas1, notas2, notas3):
    n1 = 1
    for i in range(n):
        if notas1[i] < 10:
            if notas2[i] < 10:
                print("{}({:003}) original: 0{:.2f} | final: 0{:.2f}".format(notas3[i], n1, notas1[i], notas2[i]))
            else:
                print("{}({:003}) original: 0{:.2f} | final: {:.2f}".format(notas3[i], n1, notas1[i], notas2[i]))
        else:
            if notas2[i] < 10:
                print("{}({:003}) original: {:.2f} | final: 0{:.2f}".format(notas3[i], n1, notas1[i], notas2[i]))
            else:
                print("{}({:003}) original: {:.2f} | final: {:.2f}".format(notas3[i], n1, notas1[i], notas2[i]))

        n1 += 1


if 1 <= n <= 999:
    nota_n(n, notas_ant)
    nota_n(n, notas_dep)
    n1 = compare(n, notas_ant, notas_dep, notas_aux, n1)
    print("NOTAS ALTERADAS: {}".format(n1))
    imprima(n, notas_ant, notas_dep, notas_aux)