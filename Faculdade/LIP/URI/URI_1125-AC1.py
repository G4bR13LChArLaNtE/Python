#AC1 - Professor, mas é só 0,5:

nt = float(input())
npr = float(input())

media = (nt + npr)/2

if media >= 6:
    print("aprovado")
elif (0 <= media < 6) and (nt > 2):
    print("talvez com a sub")
else:
    print("reprovado")