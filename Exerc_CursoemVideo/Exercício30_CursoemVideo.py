n =float(input("Digite um número: "))
r = (n%2)
if r != 0:
	print("{:.0f} é um número impar.".format(n))
else: 
    print("{:.0f} é um número par.".format(n))