#URI - 1044 - Múltiplos:

linha1 = input()
linha2 = linha1.split()
A = int(linha2[0])
B = int(linha2[1])


if A > B:
    if A % B == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
else:
    if B % A == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
if A == B:
    print("Sao Multiplos")

