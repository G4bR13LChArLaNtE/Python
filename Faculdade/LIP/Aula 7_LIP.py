#1) Escreva uma função que receba por parâmetro 3 números e retorne o menor valor entre eles

def menor_valor(n1,n2,n3):
    if (n1 < n2) and (n1 < n3):
        n4 = n1
    elif (n2 < n1) and (n2 < n3):
        n4 = n2
    else:
        n4 = n3
    return (n4)

n1 = int(input())
n2 = int(input())
n3= int(input())

n5 = menor_valor(n1,n2,n3)

print(n5)