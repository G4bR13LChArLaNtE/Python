#URI - 1167 - Anos bissextos:

n1 = int(input())
n2 = int(input())

def ano_biss(n1,n2):
    i = 0
    c = 0
    for i in range(n1,n2+1):
        if (i % 4 == 0 and i % 100 != 0) or  i % 400 == 0:
            print(i)
            c += 1
    return (c)


valor = ano_biss(n1, n2)
print("bissextos: {}".format(valor))
