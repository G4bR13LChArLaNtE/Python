#URI - 1040 - Média 3:

linha1 = input()


n1, n2, n3, n4 = linha1.split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

médiap = (2*n1 + 3*n2 + 4*n3 + 1*n4)/10

if médiap >= 7.0:
    print("Média: {:.1f}".format(médiap))
    print("Aluno aprovado.")
elif médiap < 5.0:
    print("Média: {:.1f}".format(médiap))
    print("Aluno reprovado.")
elif médiap >= 5.0 and médiap <= 6.9:
    print("Média: {:.1f}".format(médiap))
    print("Aluno em exame.")
    notae = float(input())
    print("Nota exame: {:.1f}".format(notae))
    médiaF = (médiap + notae)/2
    if médiaF >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Média final: {:.1f}".format(médiaF))

