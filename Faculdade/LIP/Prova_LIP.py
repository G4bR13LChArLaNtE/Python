def f1(n1,n2):
    if(n1<=n2):
        return n1
    else:
        return n2

def f2(n1,n2,n3):
    if(f1(n1,n2) <= n3):
        return (f1(n1,n2))
    else:
        return n3

n1 = float(input("Número 1: "))
n2 = float(input('Número 2: '))
n3 = float(input('Número 3: '))
r = f2(n1,n2,n3)
print(f'Resultado: {r}')