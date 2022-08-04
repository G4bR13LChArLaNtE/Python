def calc_mult(A,B):
    for i in range(A,B+1):
        for j in range(1,11):
            n = i * j
            print("{} x {} = {}".format(i,j,n))
        print("----------")

A = int(input())
B = int(input())

if A <= B:
    calc_mult(A, B)
else:
    print("Nenhuma tabuada no intervalo!")