#URI - 1037 - intervalo:

n1 = float(input())

if n1 >= 0 and n1 <= 25.0000:
    print("Intervalo [0,25]")
elif n1 >= 25.00001 and n1 <= 50.0000000:
    print("Intervalo (25,50]")
elif n1 >= 50.00000001 and n1 <= 75.0000000:
    print("Intervalo (50,75]")
elif n1 >= 75.00000001 and n1 <= 100.0000000:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")