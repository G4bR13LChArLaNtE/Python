#URI - 1065 - Pares entre 5 números:
	
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

def num_par(n1):
	cont = 0
	if n1 % 2 == 0:
		cont = cont +1
	
	return cont


cont1 = num_par(n1)
cont1 = cont1 + num_par(n2)
cont1 = cont1 + num_par(n3)
cont1 = cont1 + num_par(n4)
cont1 = cont1 + num_par(n5)

print("{} valores pares".format(cont1))