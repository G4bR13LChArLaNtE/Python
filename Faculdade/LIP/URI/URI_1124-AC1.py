#AC1 - Jogo do par ou ímpar:

n1 = int(input())
n2 = n1%2

if n2 > 0:
    ni = n1 - 2
    np = n1 + 1
    print(f"{ni} {np}")
else:
    ni = n1 - 1
    np = n1 + 2
    print(f"{ni} {np}")

