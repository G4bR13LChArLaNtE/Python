#AC2 - URI - 1168:

#Entradas de valores:

n1 = int(input())
n2 = int(input())

i1 = n1
c2 = 0
for i1 in range(n1,n2+1,1):
    i2 = 0
    c1 = 0

    for i2 in range(1, 5000, 1):
        div = i1 % i2
        if div == 0:
            c1 += 1

    if c1 == 2:
        c2 += 1
        print(i1)


    c1 = 0


primo1 = c2
print("Primos: {}".format(primo1)